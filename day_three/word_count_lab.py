# -*- coding: utf-8 -*-
# For example for the input "olly olly in come free"
# olly: 2
# in: 1
# come: 1
# free: 1

def words(sentence):
	initial = sentence.split()
	result = {}		
	for word in initial:
		if word.isdigit():
			result[int(word)]=initial.count(word)
		else:
			result[word]= initial.count(word)
	return result