

def max(arr) :
	#print(arr)
	for i in range(len(arr)-1,-1,-1):
		for j in range(i):
			if arr[i][j]>arr[i][j+1]:
				arr[i-1][j]+=arr[i][j]
			else :
				arr[i-1][j]+=arr[i][j+1]
	return(arr[0][0])

n = int(input())

for i in range(0,n):
	x=int(input())
	
	main=[]
	for i in range(0,x):
		temp= []
		x=input()
		temp = list(map(int,x.split()))
		main.append(temp)
	print(max(main))	