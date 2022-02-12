# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

n, k=map(int, input().split())

a=1
for i in range(n,n-k,-1):
    a*=i
for i in range(k, 0, -1):
    a/=i
print(int(a))
