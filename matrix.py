n=int(input())

for _ in range(n) :
	size=int(input())
	matrix=[]
	for i in range(size) :
		matrix.append(list(map(int,input().split(' ',size-1))))
	sum=0
	d={}
	for i in range(size):
		for j in range(size):
			d[matrix[i][j]] = (i,j)
	
	x1,y1=d[1]
	for k in range(2,size*size+1) :
		x2,y2=d[k]
		sum+=abs(x2-x1)+abs(y2-y1) 
		x1=x2
		y1=y2

	print(sum)

