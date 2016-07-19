n=int(input())
sols=list(map(int,input().split(' ',n-1)))
c1=0
c2=0

for i in sols:
	if i%2==0:
		c1+=1
	else:
		c2+=1


if c1>c2 :
	print("READY FOR BATTLE")
else: 
	print("NOT READY")