#!/usr/bin/env python
"""Parse raw xls files of 2020 TW election results."""

import os
import tempfile
import multiprocessing

import pandas as pd

from utils import parse_archive, gather_by_level


if __name__ == "__main__":

  outdir = "data/processed"
  if not os.path.exists(outdir):
    os.makedirs(outdir)

  # ------------------------------------- #
  # Parse presidential election raw data. #
  # ------------------------------------- #
  inzipfile1 = "data/raw/總統-各投票所得票明細及概況(Excel檔).zip"
  dfs1 = parse_archive(inzipfile1)
  presidential = gather_by_level(dfs1)

  # Write out.
  for name, df in presidential.items():
    outfile = f"presidential_{name}.csv"
    df.to_csv(os.path.join(outdir, outfile), index=False, encoding="utf-8")

  # ------------------------------------ #
  # Parse legislative election raw data. #
  # ------------------------------------ #
  inzipfile2 = "data/raw/立委-各投票所得票明細及概況(Excel檔).zip"
  dfs2 = parse_archive(inzipfile2)
