#!/usr/bin/env python
import sys

total_delay = 0
old_airline = None
total_flights = 0

for line in sys.stdin:

    line = line.strip().split('\t')
    if len(line) != 3:
        continue

    airline, delay, count = line
	
    try:
        delay = float(delay)
        count = int(count)
    except ValueError:
        continue

    if delay > 0.0:
        total_delay += 1

    if (old_airline is not None) and (old_airline != airline):
        p = (total_delay * 100) / total_flights 
        print('%s\t%s\t%f' % (old_airline, total_delay, p))
        total_delay = 0
        total_flights = 0

    old_airline = airline
    total_flights += count

if old_airline is not None:
    print('%s\t%s\t%f' % (old_airline, total_delay, p))

