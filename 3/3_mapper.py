#!/usr/bin/env python
import sys

for line in sys.stdin:

    line = line.split(',')
    
    if len(line) != 12:
        continue

    airline, delay = line[1].strip(), line[8].strip()

    if delay == "":
        delay = "0"

    print('%s\t%s\t%s' % (airline, delay, 1))
