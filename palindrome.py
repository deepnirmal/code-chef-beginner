n=int(input())

def palindrome(intnum) :
	num=str(intnum)

	if len(num)==1:
		return True

	x=len(num)-1
	for i in range(0,len(num)) :
		if num[i]==num[x]:
			x=x-1
	if x==-1:
		return True
	else:
		return False

def palin(sstr):
	string=str(sstr)
	if list(string)==list(reversed(string)) :
		return True
	else :
		return False
def palinFinal(num) :
	z=num
	y=0
	while(num):
		y=y*10+num%10
		num=int(num/10)
	if y==z:
		return True
	else:
		return False

for i in range(n) :
	num=input()
	x,y=map(int,num.split())
	sum=0
	for i in range(x,y+1) :
		k=str(i)
		if k==k[::-1] :
			sum+=i

	print(sum)	


