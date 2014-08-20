#!/usr/bin/env python

import os, os.path, json
from inspectors.utils import utils

def main():
  options = utils.options()
  report_id_history = set()
  data_dir = utils.data_dir()
  for inspector in os.listdir(data_dir):
    inspector_path = os.path.join(data_dir, inspector)
    if os.path.isdir(inspector_path):
      for year in os.listdir(inspector_path):
        year_path = os.path.join(inspector_path, year)
        if os.path.isdir(year_path):
          for report in os.listdir(year_path):
            report_path = os.path.join(year_path, report)
            if os.path.isdir(report_path):
              json_path = os.path.join(report_path, "report.json")
              if os.path.isfile(json_path):
                report_data = json.load(open(json_path, "r", encoding="utf-8"))
                report_id = report_data["report_id"]
                if report_id in report_id_history:
                  print("Duplicate report_id %s in %s" % (repr(report_id), json_path))
                report_id_history.add(report_id)
      if "global" not in options:
        report_id_history = set()

main()
