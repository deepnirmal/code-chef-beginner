n=int(input())

for _ in range(n) :
	numq=int(input())
	correctans=input()
	chefans=input()
	prize=list(map(int,input().split()))

	ctr=0
	for i in range(numq) :
		if correctans[i]==chefans[i]:
			ctr+=1
	if ctr==numq:
		print(prize[ctr])
	else:
		print(max(prize[0:ctr+1]))


