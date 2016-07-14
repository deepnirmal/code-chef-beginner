#Collections library example of Counter keyword - useful and efficient

from collections import Counter	
n=int(input())


for i in range(n) :
	num=int(input())
	dolls=[]
	for i in range(num):
		k=int(input())
		dolls.append(k)
	con=Counter(dolls)
	#print(con)
	for key,val in con.items():
		if val%2!=0 :
			print(key)
			break

#Another solution
#for i in dolls :
#		if dolls.count(i)%2!=0 :
#			print(i)
#			break	

