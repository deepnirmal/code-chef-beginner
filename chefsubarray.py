n=int(input())

for i in range(n) :
	x=int(input())
	nums=list(map(int,input().split(' ',x-1)))
	count=0
	for c in range(0,x) :
		summ=0
		product=1

		for j in range(c,-1,-1) :
			
			summ=summ+nums[j]
			product=product*nums[j]

			if summ==product :
				count+=1

	print(count)





