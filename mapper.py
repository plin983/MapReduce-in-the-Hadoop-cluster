#!/usr/bin/env python
# this line means that the script is executable,
# it calls the language interpreter to run the code inside the script
# and is the guide to find 'python'


# import the module for reading and writing data
import sys

#skip first line
next(sys.stdin)
# input is read by STDIN (standard input) and do the following for each
# input line
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # split the line by comma separator, a list is produced
    line = line.split(",")

    # assign first value of the list to the ticker
    ticker = line[1]
    
    # assign second value of the list to the ticker
    tradeDate = line[2]

    # assign the 7th value to the volumn
    tradeVolumn = line[7]
    
    # mapper prints ticker and trade price with a tab in between, which is
    # taken as input by the reducer
    if tradeDate[-4:] == '2018' :
        print ('%s\t%s' % (ticker, tradeVolumn))



