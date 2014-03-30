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

# Read the file and count occurrences of each unique word
with open(text_file, 'r') as text:
    # Count words, one line at a time
    for line in text:
        line = line.lower()
        line = line.replace('-', ' ') # Split on hyphens
        line = line.replace('—', ' ') # Split on em-dashes, too
        # create a list of words
        tempwords = line.split(None)
        for i in tempwords:
            i = i.strip(string.punctuation)
            if i != '': # No empty strings, damnit!
                if i in words:
                    words[i] += 1
                else:
                    words[i] = 1

print "WORDCOUNTS,WEIGHT" # DfR-style header
#for i in words.keys():
#    print i, words[i]
for i in sorted(words, key=words.get, reverse=True):
    print str(i)+','+str(words[i])