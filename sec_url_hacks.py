import urllib.request
import urllib.error
import re

def main():
  audit_reports_url = 'https://www.sec.gov/about/offices/oig/inspector_general_audits_reports.shtml'
  audit_reports_html = urllib.request.urlopen(audit_reports_url).read()
  report_list = re.findall(b'(?:Audit|Report)\\s+No\\.\\s+([0-9]+)', audit_reports_html)
  report_numbers = [int(b) for b in report_list if b]
  report_numbers.sort()
  print(report_numbers)
  known = set(report_numbers)

  for i in range(200, 530):
    if i in known:
      continue
    check('https://www.sec.gov/about/oig/audit/%dfin.htm' % i)
    check('https://www.sec.gov/about/oig/audit/%dfin.pdf' % i)

def check(url):
  try:
    code = urllib.request.urlopen(url).getcode()
  except urllib.error.HTTPError as e:
    code = e.getcode()
  if code != 404:
    print(url)

main()

# Results:
# https://www.sec.gov/about/oig/audit/271fin.htm
# https://www.sec.gov/about/oig/audit/384fin.pdf
# https://www.sec.gov/about/oig/audit/392fin.pdf
# https://www.sec.gov/about/oig/audit/394fin.pdf
# https://www.sec.gov/about/oig/audit/398fin.pdf
# https://www.sec.gov/about/oig/audit/399fin.pdf
# https://www.sec.gov/about/oig/audit/400fin.pdf
# https://www.sec.gov/about/oig/audit/406fin.pdf
# https://www.sec.gov/about/oig/audit/409fin.pdf
