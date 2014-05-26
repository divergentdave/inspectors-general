#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os, os.path
import re
from datetime import datetime, timezone, timedelta

def print_unicode(obj):
  s = str(obj)
  print(s.encode('ascii', 'ignore'))

def find_recurse(root, regex):
  for name in os.listdir(root):
    path = os.path.join(root, name)
    if os.path.isdir(path):
      for result in find_recurse(path, regex):
        yield result
    elif os.path.isfile(path):
      if regex.match(name):
        yield path

def all_pdf_metadata():
  json_re = re.compile(r'''.*\.json''')
  for path in find_recurse("data", json_re):
    data = json.load(open(path, 'r'))
    if "pdf_metadata" in data:
      yield data["pdf_metadata"]

def count_keys():
  key_counts = {}
  for metadata in all_pdf_metadata():
    for key in metadata:
      if key in key_counts:
        key_counts[key] = key_counts[key] + 1
      else:
        key_counts[key] = 1
  all_keys = list(key_counts.keys())
  all_keys.sort()
  for key in all_keys:
    print("%s: %d" % (key, key_counts[key]))

def parse_pdf_date(pdf_date):
  if pdf_date.startswith("D:") and len(pdf_date) == 23:
    return datetime.strptime(pdf_date.replace("'", ""), "D:%Y%m%d%H%M%S%z")
  if pdf_date.startswith("D:") and len(pdf_date) == 16:
    # At least one PDF has a tz-less creation time and a tz-aware modify time.
    # For the purposes of this script, give up and assume UTC
    return datetime.strptime(pdf_date + "+0000", "D:%Y%m%d%H%M%S%z")
  if pdf_date.startswith("D:") and len(pdf_date) == 17:
    # Assuming that Z means +0000
    return datetime.strptime(pdf_date.replace("Z", "+0000"), "D:%Y%m%d%H%M%S%z")
  # At this point I cannot be bothered to figure out timezones
  return datetime.strptime(pdf_date, "%a %b %d %H:%M:%S %Y\n").replace(tzinfo=timezone.utc)
  raise Exception("lolidk\n%s\n%d" % (pdf_date, len(pdf_date)))

def dump_dates():
  month = timedelta(days=30)
  for metadata in all_pdf_metadata():
    dates = {}
    for date_name in DATE_NAMES:
      if date_name in metadata:
        dates[date_name] = parse_pdf_date(metadata[date_name])
    if not dates:
      raise Exception("No dates!")
    pretty_dates = [datetime.strftime(date, "%Y-%m-%d") for date in dates.values()]
    first_date = min(dates.values())
    last_date = max(dates.values())
    delta = last_date - first_date
    print(delta)
    if delta > month:
      print([date_name + "=" + metadata[date_name] for date_name in DATE_NAMES if date_name in metadata])

def date_accuracy(date_name):
  buckets = [0] * 31
  count_total = 0
  count_bad = 0
  json_re = re.compile(r'''.*\.json''')
  for path in find_recurse("data", json_re):
    data = json.load(open(path, 'r'))
    if "pdf_metadata" in data:
      if date_name in data["pdf_metadata"]:
        published_on = data["published_on"]
        published_date = datetime.strptime(published_on, "%Y-%m-%d")
        published_date = published_date.replace(tzinfo=timezone.utc)
        creation_data = data["pdf_metadata"][date_name]
        creation_date = parse_pdf_date(creation_data)
        creation_date = creation_date.replace(tzinfo=timezone.utc)

        count_total = count_total + 1

        delta = published_date - creation_date
        days = abs(delta).days
        if days > 30:
          print(path, delta)
          count_bad = count_bad + 1
        else:
          buckets[days] = buckets[days] + 1
  for i in range(len(buckets)):
    print("%d days: %d PDFs" % (i, buckets[i]))
  print("%d of %d PDFs had %s off by 30 days or more" %
          (count_bad, count_total, date_name))
  print()

def main():
  for date_name in DATE_NAMES:
    date_accuracy(date_name)

DATE_NAMES = ['/CreationDate', '/CreationDate--Text', '/ModDate', '/SourceModified']

main()
