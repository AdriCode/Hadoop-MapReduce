#!/usr/bin/env python
import sys

total_count = 0
total_delay = 0.0
old_airline = None

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

    if (old_airline is not None) and (old_airline != airline):
        m = total_delay / total_count
        print('%s\t%f\t%f\t%i' % (old_airline, m, delay, count))
        total_delay = 0.0
        total_count = 0

    old_airline = airline
    total_delay += delay
    total_count += count

if old_airline is not None:
    m = total_delay / total_count
    print('%s\t%f\t%f\t%i' % (old_airline, m, delay, count))
