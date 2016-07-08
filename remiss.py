
n=int(input())

for i in range(n) :
	nums=list(map(int,input().split(' ',2)))

	minn=max(nums)

	maxx=nums[0]+nums[1]
	result=[]
	result.append(minn)	
	result.append(maxx)
	print(*result)