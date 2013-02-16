#! /usr/bin/python
import random
with open('/usr/share/dict/cracklib-small', 'r') as f:
	size_count = 0
	for line in f:
		size_count += 1
	wordnums = []
	for i in range(6):
		wordnums.append(random.randint(0, size_count))
	finished = ""
	for i in wordnums:
		f.seek(0)
		for m in range(i):
			f.readline()
		finished += f.readline().strip() + "|"
	print(finished)
