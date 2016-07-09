n=int(input())

for i in range(n) :
	r=int(input())
	x1,y1=map(int,input().split())
	x2,y2=map(int,input().split())
	x3,y3=map(int,input().split())

	x12=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
	x13=(x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)
	x23=(x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)
	rr=r*r
	if 	(x12<=rr and x13<=rr) or (x13<=rr and x23<=rr) or (x12<=rr and x23<=rr) :
		print("yes")
	else :
		print("no")

	
