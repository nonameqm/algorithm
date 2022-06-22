import sys
from collections import deque

N=int(sys.stdin.readline())
while(N>0):
    test_n, target=map(int, sys.stdin.readline().split())
    tasks=list(map(int, sys.stdin.readline().split()))
    taskarray=[]
    for i in range(len(tasks)):
        if i==target:
            taskarray.append((tasks[i], 1))
        else:
            taskarray.append((tasks[i], 0))
    tasks=deque(taskarray)


    order=0
    while(1):
        p_max=max(task[0] for task in tasks)
        item=tasks.popleft()
        if item[0]>=p_max:
            order+=1
            if item[1]==1:
                break
        else:
            tasks.append(item)

    print(order)
    N-=1