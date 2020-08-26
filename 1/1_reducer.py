#!/usr/bin/env python
import sys

min_dist = 2000
old_airline = None

for line in sys.stdin:

    data = line.strip().split('\t')
    if len(data) != 2:
        continue

    airline_ID, dist = data

    try:
        dist = float(dist)
    except ValueError:
        continue

    if (old_airline is not None) and (old_airline != airline_ID):
        print('%s\t%f' % (old_airline, min_dist))
	min_dist = 2000

    old_airline = airline_ID
    min_dist = min(min_dist, dist)

if old_airline is not None:
    print('%s\t%f' % (old_airline, min_dist))



