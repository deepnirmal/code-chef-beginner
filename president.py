n=int(input())

for _ in range(n) :
	N,K=map(int,input().split())
	ctr=0
	stud=list(map(int,input().split()))	
	ans=[]
	for i in range(N) :
			if stud.count(stud[i])>=K:
				if stud[i] not in ans :
					ans.append(stud[i])
	for i in range(N) :
		if i+1 == stud[i] :
			if stud[i] in ans :
				ans.remove(stud[i])				
#	print(ans)				
	print(len(ans))				


