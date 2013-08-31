'''untokenizes all tsv files within the folder in which this script resides'''

import re, os

path = os.getcwd()
pathcontents = os.listdir(path) 
targets = []
dirmark = ''

#figure out OS-appropriate symbol to indicate directory
env = os.name
if env == 'nt':
    dirmark = '\\'
if env == 'posix':
    dirmark = '/'

#create directory to store cleaned+compiled texts
if ('untokenized' in pathcontents) == False:
    os.mkdir(path+dirmark+'untokenized')
donedir = path+dirmark+'untokenized'

for i in pathcontents:
    if i.find(".tsv") != -1:
        targets.append(i)
if len(targets) == 0:
    print "no tsv file found in current directory"

#dammit, Leeroy!
for file in targets:
    outstring = ''
    f = open(file,"r")
    for line in f:
        outstring += re.search('.*(?=\t.*\n)', line).group(0)+" "
    f.close()
    #write untokenized version
    f = open(donedir+"{0}{1}untokenized.tsv".format(dirmark, file[:-4]), "w")
    f.write(outstring)
    f.close()
