import sys

N=int(sys.stdin.readline())

#시간 초과
# def calculate(k, n):
#     if(k==0):
#         return n
#     else:
#         result=0
#         for i in range(1, n+1):
#             result+=calculate(k-1, i)
#         return result

def calculate(k, n):
    apartment=[]
    floor_0=[i for i in range(1,n+1)]
    apartment.append(floor_0)
    for i in range(1, k+1):
        new_floor=[1]
        for m in range(1, n):
            ans = new_floor[m-1]+apartment[i-1][m]
            new_floor.append(ans)
        apartment.append(new_floor)

    return apartment[k][n-1]



while(N>0):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    print(calculate(k, n))
    N-=1