from fractions import gcd
from functools import reduce
t = int(input())
for _ in range(t):
    mylist = list(map(int,input().split()))
    del mylist[0]
    gcf = reduce(gcd,mylist)
    b = [int(x/gcf) for x in mylist]
    print(*b)
    
 