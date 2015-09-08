import vendor
vendor.add("lib")

import random
import sys
import json
import os
from generate_table import *

max_top = 100
max_bottom = 100

blockers = ",;"

if __name__ == "__main__":
	table = generate_table_from_sentences(sys.argv[1])

	w1,w2 = nonword, nonword
	i = 0
	toptext = ""
	while i < max_bottom:
	    newword = random.choice(table[(w1, w2)])
	    if newword == nonword and i > 0:
	    	break
	    elif newword == nonword:
	    	continue
	    toptext += newword + " "
	    w1, w2 = w2, newword
	    i += 1
	words = toptext.split()
	num = len(words)

	# Get the middle third and search for a blocker
	midway = num/2
	should_break = False
	for i in xrange(num/3,num*2/3):
		word = words[i]
		for c in blockers:
			if c in word:
				midway = i+1
				should_break = True
				break
		if should_break:
			break

	first = " ".join(words[:midway])
	last = " ".join(words[midway:])
	print first + "\n"
	print last