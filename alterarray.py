n=int(input())


for _ in range(n) :
	num=int(input())

	array=list(map(int,input().split()))
	ans=[0]*(num+1)	
	ans[num]=1
	for j in range(num-1,0,-1):
		if (array[j]*array[j-1])<0  :
			ans[j]=ans[j+1]+1
		else:
			ans[j]=1
	ans.pop(0)		
	for i in ans:
		print(i,end=' ')
	print()				



