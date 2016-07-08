import math

menu=[]
for i in range(0,12):
	menu.append(math.pow(2,i))

n=int(input())
result=[]

for i in range(n) :
	x=int(input())

	count=0
	while x>0 :

		for i in range(11,-1,-1):
			if menu[i]<=x :
				x=x-menu[i]
				count=count+1
				break

	result.append(count)


for i in range(len(result)):
	print(result[i])

