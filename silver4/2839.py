N=int(input())

#DP 풀이
dp=[0 for i in range(5001)]
dp[3]=1
dp[5]=1


for i in range(6, N+1, 1):
    if dp[i-3]:
        dp[i]=dp[i-3]+1
    
    if dp[i-5]:
        if(dp[i]):
            dp[i]=min(dp[i], dp[i-5]+1)
        else:
            dp[i]=dp[i-5]+1


if(dp[N]):
    print(dp[N])
else:
    print(-1)