n=int(input())

for _ in range(n) :

	A,B,K=map(int,input().split())
	ans=0
	for x in range(A,B+1) :
		string=str(x)
		flag=0
		strlen=len(string)
		for i in range(strlen):
			char=''
			for j in range(i,strlen) :
				char=char+str(string[j])
				#print(char)
				if (int(char))%K==0 :
					#print(char)
					flag=1
					break
					
		if flag!=1:
			ans+=1


	print(ans)


				
