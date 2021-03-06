#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sun Mar 30 09:19:05 2014

@author: mwilkens

Input: One fulltext file, named as first commandline argument.
Output: CSV list of wordcounts, formatted like JSTOR DfR, to stdout.

Usage: text2wordcounts <input_file.txt>
"""

import sys, string
args = sys.argv
text_file = args[1]

# Dictionary to store wordcounts
words = {}
# Set up punctuation removal
replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))

# Read the file and count occurrences of each unique word
with open(text_file, 'r') as text:
    # Count words, one line at a time
    for line in text:
        line = line.lower()
        line = line.translate(replace_punctuation)
        tempwords = line.split(None)    # create a list of words
        for i in tempwords:
            i = i.strip()               # Get rid of extra space
            if i != '':                 # No empty strings, damnit!
                if i in words:
                    words[i] += 1
                else:
                    words[i] = 1

print "WORDCOUNTS,WEIGHT"               # DfR-style header
for i in sorted(words, key=words.get, reverse=True):
    print str(i)+','+str(words[i])