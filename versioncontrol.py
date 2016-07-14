n=int(input())

for i in range(n) :
	N,M,K=map(int,input().split())	

	ignoredFiles=list(map(int,input().split(' ',M-1)))
	trackedFiles=list(map(int,input().split(' ',K-1)))


	notigonred=[]
	nottracked=[]
	for i in range(1,N+1):
		if i not in ignoredFiles :
			notigonred.append(i)
		if i not in trackedFiles :
			nottracked.append(i)		
	count1=0
	count2=0		
	for x in ignoredFiles :
		if x in trackedFiles :
			count1+=1
	for x in notigonred :
		if x in nottracked :
			count2+=1
	print(count1,count2)


