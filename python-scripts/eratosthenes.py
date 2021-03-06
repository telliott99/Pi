from math import sqrt
from collections import OrderedDict
# Sieve of Eratosthenes
# Expands by factor of 100 each time
# 1-100
# 101 - 10000, etc.

N = 100

# dict holds primes used to sieve
# and next number to test for each
D = OrderedDict({2:102})

def test_one_candidate(p,L,N):
    global D
    n = p*p
    L[n] = 0
    n += p
    while n <= N:
        L[n] = 0
        n += p
    D[p] = n

def find_next_candidate(p,L,N):
    M = int(sqrt(N))
    p += 1
    while p < N and not L[p]:
        p += 1
    if p > M:
        return False
    return p

def run_level(N):
    L = [None] + [1] * N
    # first, go through the previous primes
    for p in D:
        test_one_candidate(p,L,N)
    while True:
        test_one_candidate(p,L,N)
        p = find_next_candidate(p,L,N)
        if not p:
            break
    return L

for x in range(2,4):
    N = int(10**x)
    L = run_level(N)

def show():
    # D holds primes
    P = D.keys()
    # but so does L
    M = max(D.keys())
    for i,n in enumerate(L):
        if i > M and n:
            P.append(i)
    for i,p in enumerate(P):
        if i and not i % 10:
            print
        # x is still valid
        print str(p).rjust(x + 1),

show()
#print D


