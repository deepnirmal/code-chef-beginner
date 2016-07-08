n=int(input())


def explode(string) :
	if len(string)<=1 :
		return string
	else:
		return string[0]+" "+explode(string[1:])
def sum(x,y):
	return x+y

import functools
for i in range(n) :
	num=input()

	Sdigits=explode(num)
	digits=list(map(int,Sdigits.split()))
	summation=functools.reduce(sum,digits)
	print(summation)
