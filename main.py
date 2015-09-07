import random
import sys
import json
import os

nonword = "\n" # Since we split on whitespace, this can never be a word

# GENERATE TABLE
top_table = {}
bottom_table = {}

# Read the sample text
for meme in os.listdir("memes"):
	w1 = nonword
	w2 = nonword
	topfile = open("memes/" + meme + "/top.txt")
	for line in topfile:
		w1 = nonword
		w2 = nonword
		for word in line.split():
			top_table.setdefault( (w1, w2), [] ).append(word)
			w1, w2 = w2, word
		top_table.setdefault( (w1, w2), [] ).append(nonword) # Mark the end of the file
	topfile.close()

	w1 = nonword
	w2 = nonword
	bottomfile = open("memes/" + meme + "/bottom.txt")
	for line in bottomfile:
		w1 = nonword
		w2 = nonword
		for word in line.split():
			bottom_table.setdefault( (w1, w2), [] ).append(word)
			w1, w2 = w2, word
		bottom_table.setdefault( (w1, w2), [] ).append(nonword)
	bottomfile.close()


# print "top kek"
# for key in top_table:
# 	print key, top_table[key], len(top_table[key])
# print "bottom kek"
# for key in bottom_table:
# 	print key, bottom_table[key], len(bottom_table[key])

# GENERATE OUTPUT
max_top = 100
max_bottom = 100

w1 = nonword
w2 = nonword
print "top kek:"
i = 0
while i < max_top:
    newword = random.choice(top_table[(w1, w2)])
    if newword == nonword and i > 0:
    	break
    elif newword == nonword:
    	continue
    print newword,
    w1, w2 = w2, newword
    i += 1
print ""

w1 = nonword
w2 = nonword
print "bottom kek:"
i = 0
while i < max_bottom:
    newword = random.choice(bottom_table[(w1, w2)])
    if newword == nonword and i > 0:
    	break
    elif newword == nonword:
    	continue
    print newword,
    w1, w2 = w2, newword
    i += 1
print ""