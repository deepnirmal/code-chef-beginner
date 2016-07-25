n=int(input())

for _ in range(n) :
	num=int(input())

	ctr=0
	while num>=0 :
		ctr+=1
		num-=ctr
	print(ctr-1)	
