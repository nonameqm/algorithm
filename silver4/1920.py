# 수찾기

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


A=sorted(A)



def b_serach(target, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if target == A[m]:
        return 1
    elif target > A[m]:
        return b_serach(target, m+1, end)
    else:
        return b_serach(target, start, m-1)

for b in B:
    print(b_serach(b, 0, len(A)-1))
    