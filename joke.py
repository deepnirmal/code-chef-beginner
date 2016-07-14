n=int(input())

for i in range(n):
	num=int(input())

	for i in range(num) :
		x,y=map(int,input().split())
	ans=0
	for i in range(1,num+1):
		ans^=i
	print(ans)
