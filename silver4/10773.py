import sys
from collections import deque
K=int(sys.stdin.readline())

n_list=deque()

while(K>0):
    n=int(sys.stdin.readline())
    if(n==0):
        n_list.pop()
    else:
        n_list.append(n)
    K-=1

print(sum(n_list))
