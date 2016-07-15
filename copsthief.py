n=int(input())

for i in range(n) :
	M,x,y=map(int,input().split())
	cops=list(map(int,input().split()))
	house=list(range(1,101))
	copsview=[]
	for c in cops :
		high=c+x*y
		low=c-x*y
		if low>0:
			for i in range(low,high+1):
				copsview.append(i)
		else :
			for i in range(1,high+1):
				copsview.append(i)
	count=0			
	for h in house :
		if h not in copsview :
			count+=1
	print(count)





