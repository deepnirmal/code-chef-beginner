
str=input()
c=0
h=0
e=0
f=0
for i in str :
	if i=='C' :
		c+=1
	elif i=='H':
		if c>h :
			h+=1
	elif i=='E' :
		if h>e :
			e+=1
	elif i=='F' :
		if e>f :
			f+=1
print(f)
