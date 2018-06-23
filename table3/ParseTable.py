# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:24:15 2014
The purpose of this script is to parse the mapping of Public Law sections to U.S. Code sections.
This file parses HTML files such as http://uscode.house.gov/table3/111_148.htm
The output is a list of references, currently printing to standard output.
@author: Pablo, @williampli
"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import sys
import argparse
from collections import defaultdict
from pprint import pprint

from bs4 import BeautifulSoup

def parseTable(f):

    soup = BeautifulSoup(f, "html5lib")
    f.close()

    t = soup.find('table')
    t3 = t.find_all('tr')

    sections = defaultdict(list)
    for row in t3:
        cols = [x.get_text() for x in row.find_all("td")]
        if len(cols) > 4:
            sections[cols[2]].append(cols[3])
    return sections


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input html file')

    args = parser.parse_args()

    filename = args.input
    with open(filename, 'r') as f:
        sections = parseTable(f)
    pprint(sections)


if __name__ == "__main__":
    main()
