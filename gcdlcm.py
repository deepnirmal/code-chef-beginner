import numpy as np
np.seterr(all="ignore")
 
def gcd(a,b):
    a=np.intp(a)
    b=np.intp(b)
    while b>0:
        a,b=b,a%b
    return int(a)
 
for _ in range(int(input())):
    a,b=map(np.int32,input().split())
    g=gcd(a,b)
    l=int((a*b)/g)
    print (g,l)

  Pain in the * if you code in Python...

# To calculate the LCM you need to evaluate (A * B) / GCD(A, B). 
# With A and B limited to 1000000 you can easily overflow 32-bit int. 
# This happens in the test case and we have to enter the wrong answer to be correct. 
# Since integers in Python don't have limitations, we have to simulate 32-bit ints (like the ones in C). 
# The easiest way I managed to do that is by installing NumPy and using the int32 data type. 
# Although Python will display the result this way,
#  the interpreter will throw out an overflow exception and you will get an NZEC error when submitting the solution. 
#  Use numpy.seterr(all="ignore") to overcome this. And last, the expected output is int,
#   but using the // operator will give wrong answer. Instead, use / and convert the result to int.
#     