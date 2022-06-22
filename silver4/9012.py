#괄호문제
from collections import deque

N=int(input())


def check_vps(x):
    queue=deque()
    for ch in x:
        if ch=='(':
            queue.append(ch)
        elif ch==')':
            if '(' in queue:
                queue.pop()
            else:
                return False
        else:
            return False
    if '(' in queue:
        return False
    else:
        return True



for _ in range(N):
    data=input()
    if check_vps(data):
        print('YES')
    else:
        print('NO')