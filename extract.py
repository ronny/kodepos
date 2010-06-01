#!/usr/bin/env python

# Extract list of post codes.

import csv
import re
import sys
from BeautifulSoup import BeautifulSoup

csv_out = csv.writer(sys.stdout)

doc = sys.stdin.readlines()
soup = BeautifulSoup(''.join(doc))    
table = soup('table')[3]
rows = table('tr')

for row in rows[1:]:
    cols = row('td')
    csv_out.writerow([col.string for col in cols])
