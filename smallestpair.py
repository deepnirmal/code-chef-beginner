n=int(input())



for i in range(n) :
	x=int(input())

	nums=list(map(int,input().split(' ',x)))
	nums.sort()
	sum=nums[0]+nums[1]
	
	print(sum)

