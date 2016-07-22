n=int(input())

for i in range(n) :
	str=input()
	max_bal=0
	bal=0
	for ch in range(len(str)) :
		if str[ch]=='(': 
			bal+=1
		if str[ch]==')':
			bal-=1
		max_bal=max(max_bal,bal)
	for i in range(max_bal):	
		print("(",end='')
	for i in range(max_bal):	
		print(")",end='')
	print()
		
