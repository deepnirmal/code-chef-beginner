n=int(input())

for _ in range(n) :
	num=int(input())

	array=list(map(int,input().split()))
	ans=0
	for i in range(num) :
		summ=0

		for j in range(i,-1,-1) :
			summ=summ+array[j]

			if summ%2==0 :
				maxxlen=i-j+1
				if ans<maxxlen :
					ans=maxxlen
	print(ans)

