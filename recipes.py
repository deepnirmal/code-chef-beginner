
n=int(input())
result=[]
for i in range(n) :
	x=input()
	r=int(x[0])

	ch=list(map(int,x.split(' ',r)))
	small=ch[1]
	count=0
	for i in range(1,len(ch)) :
		if ch[i]<small :
			small=ch[i]
#	print("Small is "+str(small))
	j=2
	max=1
	while j<=small :		
		count=0
		for i in range(1,len(ch)):
			if ch[i]%j==0 :
				count=count+1

		if count==len(ch)-1:
			max=j
		j=j+1
					
#	print("max="+str(max))
	for i in range(1,len(ch)) :
		result.append(str(int(ch[i]/max))+" ")
	result.append("\n")

		
for i in result:			
	print(i,end='')	
