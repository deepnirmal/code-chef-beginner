n=int(input())

for i in range(n) :
	N,K=map(int,input().split())
	dictionary=list(map(str,input().split()))
	phrases=[]
	for i in range(K) :
		string=list(input().split())

		for j in range(1,len(string)) :
			phrases.append(string[j])
	#print(phrases)

	for d in dictionary:
		if d in phrases :
			print("YES",end=' ')
		else :
			print("NO",end=' ')