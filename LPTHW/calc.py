#!/usr/bin/python

import sys

sum = 0
for arg in sys.argv:
	try:
		sum += int(arg)
	except ValueError:
		pass

print sum