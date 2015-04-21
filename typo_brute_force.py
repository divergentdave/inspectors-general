#!/usr/bin/env python

import urllib.error
import urllib.request
import os.path
import sys
import time

ALPHABET = "0123456789-._abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_response_code(url):
  time.sleep(2)
  try:
    result = urllib.request.urlopen(url)
    return result.getcode()
  except urllib.error.HTTPError as e:
    return e.getcode()

def main():
  if len(sys.argv) != 2:
    sys.exit("Usage: %s http://www.example.com/path/bad_url.pdf" % sys.argv[0])

  bad_response_code = get_response_code(sys.argv[1])
  print("%s => %d" % (sys.argv[1], bad_response_code))

  def check(url):
    response_code = get_response_code(url)
    if response_code != bad_response_code:
      print("%s => %d" % (url, response_code))

  scheme, netloc, path, query, fragment = urllib.parse.urlsplit(sys.argv[1])
  foldername, basename = os.path.split(path)

  print("Trying single character deletions")
  for i in range(len(basename)):
    new_basename = basename[:i] + basename[i + 1:]
    new_path = foldername + "/" + new_basename
    new_url = urllib.parse.urlunsplit((scheme, netloc, new_path, query, fragment))
    check(new_url)

  print("Trying single character substitutions")
  for i in range(len(basename)):
    print("%d/%d" % (i, len(basename) - 1))
    for c in ALPHABET:
      new_basename = basename[:i] + c + basename[i + 1:]
      new_path = foldername + "/" + new_basename
      new_url = urllib.parse.urlunsplit((scheme, netloc, new_path, query, fragment))
      check(new_url)

  print("Trying single character insertions")
  for i in range(len(basename) + 1):
    print("%d/%d" % (i, len(basename)))
    for c in ALPHABET:
      new_basename = basename[:i] + c + basename[i:]
      new_path = foldername + "/" + new_basename
      new_url = urllib.parse.urlunsplit((scheme, netloc, new_path, query, fragment))
      check(new_url)

if __name__ == "__main__":
  main()
