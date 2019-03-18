import sys

from math import *
D = {'sin':sin,
     'cos':cos, 
     'tan':tan}
     
f = D[sys.argv[1]]

def pp(n,v):
    s = "%3.8f, %3.8f"
    print s % (n,v)

# --------

def close_enough(n,v,N=3):
    t = (1e-1)**N
    return abs(n-v) < t

n = 1
v = f(n)
count = 0

while not close_enough(n,v):
    count += 1
    n = v
    v = f(n)

print 'after %d rounds:' % count  
pp(n,v)




