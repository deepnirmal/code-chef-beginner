n=int(input())

for i in range(n) :
	B=int(input())

	N=int(B/2-1)
	if N>1 :
		print(int(N*(N+1)/2))
	else :
		print(N)