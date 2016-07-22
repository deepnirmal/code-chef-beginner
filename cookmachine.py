n=int(input())
import math
for i in range(n) :
	A,B=map(int,input().split())
	ctr=0
	while B%A!=0 :
		A=A//2

		ctr+=1
	while A!=B :
		A=A*2
		ctr+=1

	print(ctr)	
