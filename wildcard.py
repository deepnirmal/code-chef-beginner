n=int(input())
for i in range(n) :
		x=input()
		y=input()
		ans="Yes"
		for i in range(0,len(x)):
			if x[i]!=y[i] and x[i]!='?' and y[i]!='?' :
				ans="No"	
		print(ans)

