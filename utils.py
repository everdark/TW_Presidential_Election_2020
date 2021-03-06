import re
import glob
import tempfile
from zipfile import ZipFile
import multiprocessing

import pandas as pd


def unzip_archive(inzipfile, outdir):
  """Unzip the raw archive file.
  The resulting files may have wrongly encoded filenames for non-Chinese operating system.
  But we don't care since they only exist temporarily.
  """
  with ZipFile(inzipfile, "r") as z:
    z.extractall(outdir)
  outfiles = [filename for filename in glob.iglob(outdir + "/**/*.xls")]
  return outfiles


def parse_single_sheet(df, name):
  # Locate the main body of the table.
  header = df.columns[0]  # Also name of the first column.
  start_row_idx = df.index[df[header] == "總　計"][0] + 1
  body = df.iloc[start_row_idx:].copy()
  # Locate the candidate name columns and the rest poll columns.
  cidx = df.iloc[1].notna()
  cidx_end = cidx.where(cidx == True).reset_index(drop=True).last_valid_index() + 1
  cols_candidate = df.iloc[1][cidx].tolist()
  cols_poll = df.iloc[0][cidx_end:].tolist()
  cols = [col.replace("\n", " ") for col in cols_candidate + cols_poll]
  # Determine the top-level of the table and re-assign column names accordingly.
  if df.iloc[0][1] == "村里別":
    if df.iloc[0][2] == "投票所別":
      cols = ["Region", "Village", "Place"] + cols
    else:
      cols = ["Region", "Village"] + cols
    body.columns = cols
    # Propogate the 1st region level and remove redundant row sums.
    body["Region"].fillna(method="ffill", inplace=True)
    body = body[body["Village"].notna()].copy()
  else:
    cols = ["Region"] + cols
    body.columns = cols
  # Append top-level dichotomy.
  body["By"] = name
  body["Header1"] = re.search(r"(.*)選舉", header).groups()[0]
  body["Header2"] = re.search(r"(.*)(候選人|政黨)(.*)得票數", header).groups()[-1]
  # Reorder columns.
  topcols = ["Header1", "Header2", "By"]
  othercols = [col for col in body.columns if col not in topcols]
  body = body[topcols + othercols]
  return body


def parse_raw_xls(infile):
  """Parse the raw xls file into an analytics-friendly format."""
  xl = pd.ExcelFile(infile)
  dfs = []
  for name in xl.sheet_names:
    df = parse_single_sheet(xl.parse(name, thousands=","), name)
    dfs.append(df)
  return dfs


def parse_archive(inzipfile):
  """Parse all files in the zip archive in parallel."""
  tmpdir = tempfile.mkdtemp()
  infiles = unzip_archive(inzipfile, tmpdir)
  p = multiprocessing.Pool(multiprocessing.cpu_count() - 1)
  dfs = p.map(parse_raw_xls, infiles)
  out = [item for sublist in dfs for item in sublist]
  return out


def gather_by_level(dfs):
  """Vertically append tables by different counting levels.
  Note that this only applies to presidential election data.
  """
  dfs_region = []
  dfs_village = []
  dfs_pplace = []
  for df in dfs:
    header = df["Header2"].values[0]
    if "各鄉(鎮、市、區)" in header:
      dfs_region.append(df)
    elif "各村(里)" in header:
      dfs_village.append(df)
    elif "各投開票所" in header:
      dfs_pplace.append(df)
    else:
      counties = df.reset_index(drop=True)
  regions = pd.concat(dfs_region).reset_index(drop=True)
  villages = pd.concat(dfs_village).reset_index(drop=True)
  pplaces = pd.concat(dfs_pplace).reset_index(drop=True)
  return {"counties": counties, "regions": regions, "villages": villages, "pplaces": pplaces}


def gather_by_class(dfs):
  """Vertically append legislative tables by class.
  Note that aborigine and party-list are only avail in polling place level.
  But constituency has both polling place and village level.
  We will drop the village level since it is also contained by the polling level.
  """
  cur_header = None
  cur_dfs = []
  out = dict()
  for df in dfs:
    # Clean up header since the format is a bit incinsistent for different types
    if "區域立法委員" in df["Header1"].iloc[0]:
      if "各投開票所" not in df["Header2"].iloc[0]:
        continue
      else:
        h1 = "第10屆區域立法委員"
    else:
      h1 = df["Header1"].iloc[0]
    this_header = h1 + ":" + df["By"].iloc[0]
    if this_header != cur_header:
      if len(cur_dfs):
        out[cur_header] = pd.concat(cur_dfs)
        cur_dfs = []
      cur_header = this_header
      cur_dfs.append(df)
    else:
      cur_dfs.append(df)
  # Re-group party-list results.
  party_list_key = "第10屆全國不分區及僑居國外國民立法委員"
  pl = []
  ple = [k for k in out.keys() if party_list_key in k]
  for k in ple:
    pl.append(out.pop(k))
  out[party_list_key] = pd.concat(pl)
  # Re-group highland aborigine results.
  highland_key = "第10屆山地原住民立法委員"
  hl = []
  hle = [k for k in out.keys() if highland_key in k]
  for k in hle:
    hl.append(out.pop(k))
  out[highland_key] = pd.concat(hl)
  # Re-group lowland aborigine results.
  lowland_key = "第10屆平地原住民立法委員"
  ll = []
  lle = [k for k in out.keys() if lowland_key in k]
  for k in lle:
    ll.append(out.pop(k))
  out[lowland_key] = pd.concat(ll)
  return out


def zh_to_en(s, map_file="data/county_name.csv"):
  """Translate traditional Chinese to English (for output filename)."""
  mappings = pd.read_csv(map_file)
  mappings = dict(zip(mappings["county_zh"], mappings["county_en"].str.lower().str.replace(" ", "_")))
  replacements = {
    r"第10屆山地原住民立法委員": "highland_aborigine",
    r"第10屆平地原住民立法委員": "lowland_aborigine",
    r"第10屆區域立法委員": "constituency",
    r"第10屆全國不分區及僑居國外國民立法委員": "partylist",
    r":": "_",
    r"第": "_",
    r"選舉區": ""
  }
  replacements.update(mappings)
  replacements = dict((re.escape(k), v) for k, v in replacements.items())
  pat = re.compile("|".join(replacements.keys()))
  return pat.sub(lambda m: replacements[re.escape(m.group(0))], s)
