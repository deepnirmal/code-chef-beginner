
n=int(input())

for i in range(n) :
	exp=input()
	postfix=[]
	stack=[]
	top=0
	stack.append('#')
	for i in range(len(exp)) :
		x=exp[i]
		if x=='('or x=='+' or x=='-' or x=='*' or x=='/' or x=='^' :
			top=top+1
			stack.insert(top,x)
		elif x==')' :
			while stack[top]!='(':
				print(stack[top],end='')		
				top=top-1
			top=top-1	
		else :
			print(x,end='')
#	print(stack)
	while stack[top]!='#':
		print(stack[top],end='')
		top=top-1	
	print()






