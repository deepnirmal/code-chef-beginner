n=int(input())
H=50
C=0.7
T=5600
for i in range(n): 
	nums=list(input().split())
	h=int(nums[0])
	c=float(nums[1])
	t=int(nums[2])
	grade=0
	if h>H and c<C and t>T :
		grade=10
	elif  h>H and c<C :
		grade=9
	elif c<C and t>T :
		grade=8
	elif  h>H and t>T :
		grade=7
	elif h>H or c<C or t>T :
		grade=6
	else:
		grade=5
	print(grade)
