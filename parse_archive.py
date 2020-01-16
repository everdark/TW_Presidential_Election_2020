#!/usr/bin/env python
"""Parse raw xls files of 2020 TW election results."""

import os
import shutil
import pandas as pd
from utils import parse_archive, gather_by_level, gather_by_class


if __name__ == "__main__":

  # ------------------------------------- #
  # Parse presidential election raw data. #
  # ------------------------------------- #
  outdir1 = "data/processed/presidential"
  if not os.path.exists(outdir1):
    os.makedirs(outdir1)
  inzipfile1 = "data/raw/總統-各投票所得票明細及概況(Excel檔).zip"
  dfs1 = parse_archive(inzipfile1)
  presidential = gather_by_level(dfs1)

  # Write out.
  for name, df in presidential.items():
    outfile = f"presidential_{name}.csv"
    df.to_csv(os.path.join(outdir1, outfile), index=False, encoding="utf-8")

  # Zip.
  shutil.make_archive("data/out/presidential", "zip", outdir1)

  # ------------------------------------ #
  # Parse legislative election raw data. #
  # ------------------------------------ #
  outdir2 = "data/processed/legislative"
  if not os.path.exists(outdir2):
    os.makedirs(outdir2)
  inzipfile2 = "data/raw/立委-各投票所得票明細及概況(Excel檔).zip"
  dfs2 = parse_archive(inzipfile2)
  legislative = gather_by_class(dfs2)
  # Write out.
  for name, df in legislative.items():
    outfile = f"legislative_{name}.csv"
    df.to_csv(os.path.join(outdir2, outfile), index=False, encoding="utf-8")

  # Zip.
  shutil.make_archive("data/out/legislative", "zip", outdir2)
