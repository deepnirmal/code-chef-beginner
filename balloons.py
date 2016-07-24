n=int(input())

for _ in range(n) :
	str=input()
	ctra=0
	ctrb=0
	for i in str:
		if i=='a':
			ctra+=1
		else:
			ctrb+=1

	print(min(ctra,ctrb))
