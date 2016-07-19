n=int(input())

for i in range(n) :
	N,M,k=map(int,input().split())
	diff=abs(N-M)
	if diff<=k :
		print(0)
	else :
		print(diff-k)