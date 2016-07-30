n=int(input())

for _ in range(n) :
	A=input()
	B=input()
	flag=False
	for i in range(len(A)) :
		for j in range(len(B)) :
			if A[i]==B[j] :
				flag=True
				
	if flag==True :
		print("Yes")
	else:
		print("No")
