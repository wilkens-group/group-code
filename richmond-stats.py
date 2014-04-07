#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 15:15:10 2014

@author: mwilkens

Reads XML files from digitized Richmond Dispatch. Outputs to stdout in
tab separated format: date, page count, and word count.

Usage: ./richmond-stats.py <input.xml>
"""

import sys
from bs4 import BeautifulSoup

args = sys.argv
text_file = args[1]

with open (text_file, 'r') as dispatch:
    soup = BeautifulSoup(dispatch)
    pubdate = str(soup.teiheader.filedesc.sourcedesc.biblfull.publicationstmt.date.get('when'))
    pagecount = str(soup.teiheader.filedesc.sourcedesc.biblfull.extent.renderContents().split()[0])
    wordcount = 0
    text = soup.find('text')
    for i in text.stripped_strings:
        words = i.split()
        wordcount += len(words)
    print pubdate+'\t'+pagecount+'\t'+str(wordcount)