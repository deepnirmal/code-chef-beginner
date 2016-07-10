n=int(input())
def check(num) :
	flag=0
	for i in range(2,num) :
		if num%i==0:
			flag=1
			break
	if flag==1 :
		print("no")
	else :
		print("yes")


for i in range(n) :
	num=int(input())
	check(num)
