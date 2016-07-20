n=int(input())

for i in range(n) :
	m=int(input())
	seq=list(map(int,input().split(' ',m-1)))
	n=int(input())
	sub=list(map(int,input().split(' ',n-1)))
	
	x=0
	y=0
	while x<len(seq) and y<len(sub)	:
		if seq[x]==sub[y]:
			x+=1
			y+=1
		else:
			x+=1

	if y==len(sub) :
		print("Yes")
	else:
		print("No")
