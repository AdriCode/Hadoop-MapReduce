#!/usr/bin/env python
import sys

old_airline = None
dif = []
dev = 0.0

for line in sys.stdin:

    line = line.strip().split('\t')
    if len(line) != 4:
        continue

    airline, m, delay, count = line

    try:
        count = int(count)
        delay = float(delay)  
        m = float(m)
    except ValueError:
        continue

    if (old_airline is not None) and (old_airline != airline):
        dev = ( sum(dif) / count )**0.5
        print('%s\t%f\t%f' % (old_airline, m, dev))
        dif = []

    old_airline = airline
    dif.append( ( (delay-m)**2) )

if (old_airline is not None):
    dev = ( sum(dif) / count )**0.5
    print('%s\t%f\t%f' % (old_airline, m, dev))
