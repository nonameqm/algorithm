import sys
from collections import deque

N, K=map(int, sys.stdin.readline().split())

n_list=deque([[i, 0] for i in range(1, N+1)])


y_list=[]
index=0
count=0
while(1):
    if len(y_list)==N:
        break

    if n_list[index][1]==0:
        count+=1
        if count%K==0:
            n_list[index][1]=1
            y_list.append(n_list[index][0])

    index=(index+1)%N



print("<",end='')
for i in range(len(y_list)-1):
    print("%d, "%y_list[i], end='')
print(y_list[-1], end='')
print(">")