n=int(input())
import functools

if n>=1 and n<=1000 :
	for i in range(n) :
		string=input()
		if len(string)>=1 and len(string)<=50 :
			count=1
			for i in string :
				if string.count(i)>count:
					count=string.count(i)
			if len(string)-count==count :
				print("YES")
			else :
				print("NO")