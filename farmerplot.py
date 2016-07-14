n=int(input())


def gcd(x,y) :
	while y>0:
		x,y=y,x%y
	return x


for i in range(n) :
	x,y=map(int,input().split()) 

	gcdval=gcd(x,y)
	print(int(x*y/(gcdval*gcdval)))
