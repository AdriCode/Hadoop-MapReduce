#!/usr/bin/env python
import sys

counter = 0

for line in sys.stdin:

    if counter != 0:

	data = line.split(',')
    
    	if len(data) != 12:
        	continue

    	airline_ID, delay = data[1].strip(), data[8].strip()

    	if delay == "":
        	delay = "0"
	
	print('%s\t%s\t%s' % (airline_ID, delay, 1))

    counter += 1
