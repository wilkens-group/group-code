'''
checks for texts to clean and compile.
they should be placed in numbered folders within the "raw" folder
results will be placed in a folder called "cleaned"

assumes a limited number of ways to mark the end of sentences.
included semi-colon as end of sentence because the clauses are independent.
tokenization counted words like "Mr." as one unit, so there should be no need to control for abbreviations.
It would be a much more involved task to fragments at the beginning that start with proper names 
(hence first word would be capitalized though it's not the start of a sentence)
I am therefore assuming that it'll be highly unlikely for us to catch a fragment at a capitalized word.
aug212013sw
'''

import re, os

path = os.getcwd()
parentdircontents = os.listdir(re.search(r'.+(?=[\\/])', path).group(0)) #go up one directory and list its contents; should work on both win and linux


rawdir = ''
cleaneddir = ''
targets = []
dirmark = ''

#figure out OS-appropriate symbol to indicate directory
env = os.name
if env == 'nt':
    dirmark = '\\'
if env == 'posix':
    dirmark = '/'
    
#check if raw folder is there to be processed
if "raw" in parentdircontents:
    rawdir = re.search(r'.+[\\/]', path).group(0) + "raw"
    contents = os.listdir(rawdir)
    #weeds out non-directories and uninteresting directories in the raw folder.  just in case.
    for i in contents:
        if i.isdigit():
            targets.append(i)
#if there's no "raw" folder or numbered folders within "raw", then there's nothing to clean
    if len(targets) == 0: #nothing within "raw" folder
            print "nothing to clean"
else: #no "raw" folder
    print "nothing to clean"
    
#create directory to store cleaned+compiled texts
if ('cleaned' in parentdircontents) == False:
    os.mkdir(re.search(r'.+[\\/]', path).group(0)+'cleaned')
cleaneddir = re.search(r'.+[\\/]', path).group(0) + "cleaned"

#LEEROY JENKINS!!!!!
for dir in targets:
    outstring = ''
    workingdir = rawdir + dirmark + dir
    os.chdir(workingdir)
    rawfiles = os.listdir(workingdir)
    for file in rawfiles:
        f = open(file,"r")
        text = f.read()
        f.close()
        #<-----------identify sentences and purge the rest------------->
        if text[0].isupper():
            newtext = re.search('.*[.!?;]', text, re.DOTALL).group(0)
        else:
            newtext = re.search('(?<=[.!?;]\tO\n).*[.!?;]',text,re.DOTALL).group(0)
        outstring += newtext+ "\tO\n"
    f = open(cleaneddir+"{0}{1}.tsv".format(dirmark, dir), "w")
    f.write(outstring)
    f.close()

