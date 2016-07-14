n=int(input())

for i in range(n):
	string1=input()
	string2=input()

	if len(string1)== len(string2) and len(string1)>=1 and len(string2)<=100:
		x=len(string1)
		min=0
		max=0
		for i in range(x) :
			if string1[i]=='?' and string2[i]=='?' :
				max+=1
			elif string2[i]=='?' or string1[i]=='?':
				max+=1
			elif string1[i]!=string2[i] :
				min+=1
				max+=1
			else :
				continue
		print(min,max)
