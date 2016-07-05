
def findInverse(a) :
	inverse=[]
	for i in range(1,len(a)+1):
		pos=search(i,a)
		#print(pos)	
		inverse.append(pos)
	return inverse


def search(x,array) :
	for i in range(len(array)):
		if array[i] == x :
			return i+1

while True:

	n=int(input())

	if n==0 :
		break

	x=input()

	array=list(map(int,x.split(' ',n-1)))


#	ins=findInverse(array)

	#print(ins)
	flag=1
	for i in range(1,n+1) :
		if i!=array[array[i-1]-1] :
			flag=0
			break


	if flag==0 :
		print("not ambiguous")
	else :
		print("ambiguous")
