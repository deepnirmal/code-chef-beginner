
import math
import functools
n=int(input())
def square(num):
	return num*num

for i in range(n) :
	nums=list(map(int,input().split()))
	#print(nums)
	sqrdNums=list(map(square,nums))
	max=sqrdNums[1]+sqrdNums[0]
	min=sqrdNums[1]-sqrdNums[0]
	result=[]
	result.append(math.sqrt(min))
	result.append(math.sqrt(max))
	


	print(*result)

