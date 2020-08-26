#!/usr/bin/env python
import sys

old_airline = None
list_delays = []

for line in sys.stdin:

    line = line.strip().split('\t')

    if len(line) != 2:
        continue

    airline, delay = line

    try:
        delay = float(delay)
    except ValueError:
        continue

    if delay < = 0.0:
	continue

    if (old_airline is not None) and (old_airline != airline):
        list_delays.sort(reverse=True)
        print('%s\t%s' % (old_airline, list_delays[:10]))
        list_delays = []

    old_airline = airline
    list_delays.append(delay)

if old_airline is not None:
    list_delays.append(delay)
    list_delays.sort(reverse=True)
    print('%s\t%s' % (old_airline, list_delays[:10]))
