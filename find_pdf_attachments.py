#!/usr/bin/env python

import os, os.path, subprocess, tempfile, shutil
import logging
from inspectors.utils import utils

def main():
  for dirpath, dirnames, filenames in os.walk(utils.data_dir()):
    for filename in filenames:
      _, extension = os.path.splitext(filename.lower())
      if extension == ".pdf":
        try:
          original = os.path.join(dirpath, filename)
          decrypted_file, decrypted_path = tempfile.mkstemp(suffix=".pdf")
          os.close(decrypted_file)
          decrypted_file = None
          logging.debug("Decrypting %s to %s" % (original, decrypted_path))
          subprocess.check_call(["qpdf", "--decrypt", original, decrypted_path])
          try:
            extract_dir = tempfile.mkdtemp()
            logging.debug("Extracting %s to %s" % (decrypted_path, extract_dir))
            subprocess.check_call(["pdftk", decrypted_path, "unpack_files"], cwd=extract_dir)
            attachments = os.listdir(extract_dir)
            if attachments:
              print("%s has the following attachments: %s" % (original, ', '.join(attachments)))
          finally:
            shutil.rmtree(extract_dir)
        finally:
          try:
            if decrypted_file:
              os.close(decrypted_file)
              decrypted_file = None
          finally:
            os.remove(decrypted_path)

main()
