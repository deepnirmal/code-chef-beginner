n=int(input())


for _ in range(n) :
	movies=int(input())

	L=list(map(int,input().split()))
	R=list(map(int,input().split()))
	maxxPro=0
	maxR=0
	pos=0
	for i in range(len(L)) :
		pro=L[i]*R[i]
		if pro>maxxPro:
			maxxPro=pro
			maxR=R[i]
			pos=i
		elif pro==maxxPro :
			if maxR<R[i] :
				maxR=R[i]
				pos=i
	
	print(pos+1)
