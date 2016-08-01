test = int(input())
names = input().split()
male = []
female = []
count = 0
for name in names:
	if name.endswith('ka'):
		male.append(name[:-2])
	elif name.endswith('ki'):
		female.append(name[:-2])
for name in male:
	if name in female:
		count += 1
		female.remove(name)
print(count) 
 