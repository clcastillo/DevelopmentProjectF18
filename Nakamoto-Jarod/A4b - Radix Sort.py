# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:07:04 2018

@author: Jarod
"""

#load in text file
inflobj = open('BookText.txt.txt','r')
lines = inflobj.readlines()
text = []
for i in range(0, len(lines)):
	text.extend(lines[i].split())
	print(text)

#create buckets
numCharacters = 60
buckets = [[] for i in range(0, numCharacters)]

#find longest element
max_length = len(text[0])
for i in range(1, len(text)):
	temp = len(text[i])
	if temp > max_length:
		max_length = temp
		
print("Maximum length: " + str(max_length))

#make everything the same length
for i in range(0, len(text)):
	#print(text[i])
	text[i] = '{:>{}s}'.format(text[i], max_length)
	#print(text[i])
	
print(text)

print()

i = 0
while i < max_length:
	#fill buckets
	for m in range(0,len(text)):
		j = m + 97
		if(i == 0):
			buckets[int(ord(text[j][-1*(i+1):])-65)].append(text[j])
		else:
			buckets[int(ord(text[j][-1*(i+1):-1*i])-65)].append(text[j])
	text.clear()
	#empty buckets
	for m in range(0, numCharacters):
		j = m + 97
		for k in range(0, len(buckets[j])):
			text.append(buckets[j].pop(0))
	
	i = i+1

print(text)	