n=int(input())

for _ in range(n) :
	num=int(input())

	str=input()
	r=0
	g=0
	b=0
	for i in range(len(str)):
		if str[i]=='R':
			r+=1
		elif str[i]=='G':
			g+=1
		else:
			b+=1
	maxx=0		
	if r>=b and r>=g:
		maxx=r
	elif b>=g :
		maxx=b
	else:
		maxx=g
	print(len(str)-maxx)