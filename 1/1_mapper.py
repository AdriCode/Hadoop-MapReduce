#!/usr/bin/env python
import sys

for line in sys.stdin:

    data = line.split(',')
    
    if len(data) != 12:
        continue

    airline_ID, dist = data[1].strip(), data[10].strip()
    
    if dist == "":
        dist = "0"

    print('%s\t%s' % (airline_ID, dist))

