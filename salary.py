n=int(input())
import math
for i in range(n) :
	sal=int(input())
	gross=0
	if sal<1500:
		hra=sal*0.10
		da=sal*0.90

	else:
		hra=500
		da=sal*0.98
	gross=sal+hra+da

	print('%g'%gross)

