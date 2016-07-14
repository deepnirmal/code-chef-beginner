n=int(input())

for i in range(n) :
	no=int(input())

	nums=list(map(int,input().split(' ',no-1)))
	mini=10000000
	for num in nums :
		if num<mini :
			mini=num

	cost=mini*(len(nums)-1)		
	print(cost)

