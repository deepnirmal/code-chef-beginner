n=int(input())

for i in range(n) :
	num=int(input())
	string=input()
	
	if 'Y' in string :
		print("NOT INDIAN")
	elif 'I' in string :
		print("INDIAN")
	else: 
		print("NOT SURE")