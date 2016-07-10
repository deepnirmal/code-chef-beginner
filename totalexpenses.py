n=int(input())

for i in range(n) :
	x,y=map(int,input().split())
	if x>1000 :
		val=x*y-x*y*0.1

	else:
		val=x*y*1.0
	print(format(val,'.6f'))