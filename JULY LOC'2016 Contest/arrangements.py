n=int(input())

def fact(x) :
	factt=1
	M = 1000000007
	for i in range(1,x+1):
		factt=(factt*i)%M
	return factt 
	
for _ in range(n) :
	string=input()
	x=len(string)
	unique=[]
	for i in range(x) :
		if string[i] not in unique :
			unique.append(string[i])
#	print(unique)	
	teams=len(unique)	
	if teams==x or teams==1:
		print(fact(x))
	else: 
		ans=fact(teams)
		for z in unique :
			count=string.count(z)
			if count>1 :
				ans*=fact(count)
		print(ans)		

