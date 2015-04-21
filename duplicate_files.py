#!/usr/bin/env python

import hashlib
import os, os.path

from inspectors.utils import utils

class Deduplicator(object):
  def __init__(self):
    self.hashes_to_names = {}

  def add_and_check_file(self, filename):
    hash = self.file_to_hash(filename)
    if hash in self.hashes_to_names:
      self.hashes_to_names[hash].append(filename)
      return self.hashes_to_names[hash]
    else:
      self.hashes_to_names[hash] = [filename]
      return None

  def file_to_hash(self, path):
    hash = hashlib.sha256()
    with open(path, 'rb') as f:
      message = None
      while message != b'':
        message = f.read(1024 * 1024)
        hash.update(message)
    return hash.digest()

def main():
  dedup = Deduplicator()
  for dirpath, dirnames, filenames in os.walk(utils.data_dir()):
    for filename in filenames:
      result = dedup.add_and_check_file(os.path.join(dirpath, filename))
      if result:
        print("Duplicate files: " + ", ".join(result))

main()
