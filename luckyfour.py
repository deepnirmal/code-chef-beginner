n=int(input())
for i in range(n) :
	num=input()
	x=len(num)
	count=0
	for i in range(0,x) :
		if num[i]=='4' :
			count+=1
	print(count)