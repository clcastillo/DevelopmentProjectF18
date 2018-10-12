ARRAY_SIZE = 69

for i in range(0,ARRAY_SIZE):
    f = open("BookText.txt.txt", "r")
    list = []
    for line in f:
        list.append(line)
print(list)

buckets = [ [] for x in range(27) ]

#find max/analyze length/pad with zeros
max = ""
for i in range(0,len(list)):
  if(len(list[i]) >len(max)):
    max = list[i]
    
print("Length of max element: " + str(len(max)))
maxLength = len(max)

for i in range(0,len(list)):
  list[i] = list[i].ljust(maxLength)
  
print(list)

i = 0
while i < maxLength:
  for j in range(0,len(list)):
    if(i == 0):
      buckets[(ord(list[j][-1 * (i + 1):]))%26].append(list[j])
    else:
      buckets[(ord(list[j][-1 * (i + 1):-1*i]))%26].append(list[j])
  list.clear()
  
  del list[:]
  
  for j in range(0,26):
    for k in range(0,len(buckets[j])):
        list.append(buckets[j].pop(0))
  
  i+=1
print(list)
