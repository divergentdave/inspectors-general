#!/usr/bin/env python

import os, os.path
from inspectors.utils import utils

skip_extensions = ('.json', '.txt')

def main():
  ext_counts = {}
  for dirpath, dirnames, filenames in os.walk(utils.data_dir()):
    for filename in filenames:
      _, extension = os.path.splitext(filename.lower())
      if extension in skip_extensions: continue
      if extension in ext_counts:
        ext_counts[extension] = ext_counts[extension] + 1
      else:
        ext_counts[extension] = 1
  items = sorted(ext_counts.items(), key=lambda x: x[1], reverse=True)
  for item in items:
    print("%s: %d" % item)

main()
