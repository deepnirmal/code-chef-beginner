n=int(input())

for i in range(n) :
	num=input()

	if num==num[::-1] :
		print("wins")
	else:
		print("losses")

