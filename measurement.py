n=int(input())
import functools
def sum(x,y) :
	return x+y
for _ in range(n) :
	N,K=map(int,input().split())

	values=list(map(int,input().split()))

	values.sort()


	summ=0
	#print(values)
	for i in range(K,len(values)-K) :
		summ=summ+values[i]

	#print(summ)
	ans=float(summ/(len(values)-2*K))
	print("%.6f"%ans)


