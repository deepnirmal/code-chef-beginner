import math
n=int(input())

for i in range(n) :
	ans=0
	n,k=map(int,input().split())
	for i in range(1,k+1):
		ans=max(ans,n%i)
	print(ans)
