#!/usr/bin/env python
import sys
from ast import literal_eval as l_e

old_airline = None

for line in sys.stdin:

    line = line.strip().split('\t')
    if len(line) != 2:
        continue

    airline, delays = line
    delays = l_e(delays)
	
    if (old_airline is not None) and (old_airline != airline):
        print('%s\t%s' % (airline, delays))

    old_airline = airline


