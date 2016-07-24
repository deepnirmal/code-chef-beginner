n=int(input())

for _ in range(n) :
	x=int(input())

	nums=list(map(int,input().split(' ',x-1)))
	temp=0
	count=0
	for i in range(0,len(nums)-1) :
		if nums[i]<=nums[i+1]:
			temp+=1
			#print(temp)
		else:
			for j in range(0,temp+1):
				count+=j
			temp=0


	for j in range(0,temp+1):
			count+=j
	

	print(count+len(nums))
