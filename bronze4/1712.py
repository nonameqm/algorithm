import math

a, b, c=map(int , input().split())
if(c-b<=0):
    print(-1)
    exit()
n=a/(c-b)
if n>0:
    print(int(n+1))
else:
    print(-1)