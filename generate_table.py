import random
import sys
import json
import os
import nltk
from nltk.tokenize import sent_tokenize

nonword = "\n" # Since we split on whitespace, this can never be a word

def generate_tables():
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
	return {
		"top": top_table,
		"bottom": bottom_table
	}

def generate_table(filename):
	# GENERATE TABLE
	table = {}

	# Read the sample text
	w1 = nonword
	w2 = nonword
	f = open(filename)
	text = f.read()
	f.close()
	for word in text.split():
		table.setdefault( (w1, w2), [] ).append(word)
		w1, w2 = w2, word
	table.setdefault( (w1, w2), [] ).append(nonword) # Mark the end of the file

	return table

def generate_table_from_sentences(filename):
	table = {}

	w1 = nonword
	w2 = nonword
	f = open(filename)
	text = f.read().decode('utf-8')
	f.close()
	sentences = sent_tokenize(text)
	for sentence in sentences:
		w1 = nonword
		w2 = nonword
		for word in sentence.split():
			table.setdefault( (w1,w2), [] ).append(word)
			w1,w2 = w2,word
		table.setdefault( (w1,w2), [] ).append(nonword)
	return table