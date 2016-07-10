n=int(input())

for i in range(n) :
	x,y,z=map(int,input().split())

	if x>0 and y>0 and z>0:
		if x+y+z==180:
			print("YES")
		else: 
			print("NO")
	else:
		print("NO")