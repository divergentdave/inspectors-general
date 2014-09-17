#!/usr/bin/env python

import datetime
import logging
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from utils import utils, inspector

# http://www.gpo.gov/oig/
archive = 2004

# options:
#   standard since/year options for a year range to fetch from.
#
# Notes for IG's web team:
#

AUDIT_REPORTS_URL = "http://www.gpo.gov/oig/audits.htm"
SEMIANNUAL_REPORTS_URL = "http://www.gpo.gov/oig/semi-anual.htm"

HEADER_TITLES = [
  'Report #',
  'Date',
]

REPORT_URLS = {
  "audit": AUDIT_REPORTS_URL,
  "semiannual_report": SEMIANNUAL_REPORTS_URL,
}

def run(options):
  inspector.save_report({
    'url': 'http://www.gpo.gov/oig/doesyour404work',
    'file_type': 'htm',
    'published_on': '2014-01-01',
    'report_id': '404_test',
    'title': '404 test',
    'inspector': 'gpo',
    'inspector_url': 'http://www.gpo.gov/oig/',
    'agency': 'gpo',
    'agency_name': 'Government Printing Office'
  })
  return

  year_range = inspector.year_range(options, archive)

  # Pull the reports
  for report_type, url in REPORT_URLS.items():
    doc = BeautifulSoup(utils.download(url))
    results = doc.select("div.section1 div.ltext > table tr")
    if not results:
      results = doc.select("td.three-col-layout-middle div.ltext > table tr")
    if not results:
      raise AssertionError("No report links found for %s" % url)
    for result in results:
      if (not result.text.strip() or
          result.find("th") or
          result.find("strong") or
          result.contents[1].text in HEADER_TITLES
        ):
        # Skip header rows
        continue
      report = report_from(result, url, report_type, year_range)
      if report:
        inspector.save_report(report)

def report_from(result, landing_url, report_type, year_range):
  title = result.select("td")[-1].text

  if "contains sensitive information" in title:
    unreleased = True
    report_url = None
    report_id = "-".join(title.split())[:50]
  else:
    unreleased = False
    link = result.find("a")
    report_id = link.text
    report_url = urljoin(landing_url, link.get('href'))

  estimated_date = False
  try:
    published_on = datetime.datetime.strptime(report_id.strip(), '%m.%d.%y')
  except ValueError:
    # For reports where we can only find the year, set them to Nov 1st of that year
    published_on_year_text = result.find_previous("th").text
    published_on_year = int(published_on_year_text.replace("Fiscal Year ", ""))
    published_on = datetime.datetime(published_on_year, 11, 1)
    estimated_date = True

  if published_on.year not in year_range:
    logging.debug("[%s] Skipping, not in requested range." % report_url)
    return

  report = {
    'inspector': 'gpo',
    'inspector_url': 'http://www.gpo.gov/oig/',
    'agency': 'gpo',
    'agency_name': 'Government Printing Office',
    'file_type': 'pdf',
    'type': report_type,
    'report_id': report_id,
    'url': report_url,
    'title': title,
    'published_on': datetime.datetime.strftime(published_on, "%Y-%m-%d"),
  }
  if estimated_date:
    report['estimated_date'] = estimated_date
  if unreleased:
    report['unreleased'] = unreleased
    report['landing_url'] = landing_url
  return report

utils.run(run) if (__name__ == "__main__") else None
