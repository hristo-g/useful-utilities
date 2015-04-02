#!/usr/bin/python

from numpy import array
from sys import argv

import re

def findOccurrences(s, ch):
    if (type(ch) == set):
        return [i for i, letter in enumerate(s) if letter in ch]
    elif (type(ch) == str):
        return [i for i, letter in enumerate(s) if letter == ch]
    else:
        return None

if (len(argv) == 2):
    fileName = argv[1]
else:
    fileName = 'notes.tex'

dLine = {}

sChars = set(['%', '#', '_'])

with open(fileName, 'r') as f:
    for l, line in enumerate(f):
        l += 1
        line = line.strip()

        originalLine = line

        if (len(line) == 0):
            continue

        if (line[0] != '%'):
            line = re.sub('{#\d+}', '', line)
            line = re.sub('{sec:.+}', '', line)

            last = line.rfind('%')
            if (last > 0):
                while (line[last] == '%'):
                    last -=1

                if (line[last] == ' '):
                    line = line[:last+1]

            lIds = findOccurrences(line, sChars)

            if (len(lIds) == 0 or line[0] == '%'):
                continue

            if (0 in lIds):
                dLine[l] = originalLine

            lIds = array(lIds)
            lIds -= 1

            aLine = array(list(line))

            if (any(aLine[lIds] == '\\') == False):
                dLine[l] = originalLine
                #continue # Just in case something gets added beyond this point.
            

for l in sorted(dLine.keys()):
    line = dLine[l]

    for ch in sChars:
        line = line.replace(ch, '\033[1;33m%c\033[1;m' % ch)
    
    print('\033[1;42m%d:\033[1;m %s' %(l, line))

if (dLine == {}):
    print('All diagnostics passed successfully!')
