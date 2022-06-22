import sys

A, B=map(int, sys.stdin.readline().split())

def gcd(A, B):
    while(B!=0):
        n=A%B
        A=B
        B=n
    
    return A

if A<B:
    A, B=B, A


g=gcd(A, B)
l=A*B/g
print(g)
print(int(l))