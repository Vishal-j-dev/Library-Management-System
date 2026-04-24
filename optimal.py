coin=[1,2,3]

c=5
n=len(coin)
dp=[[0]*(c+1)for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=1

for i in range(1,n+1):
    for j in range(c+1):
        if j<coin[i-1]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-coin[i-1]]
    for i in range(n+1):

print(dp[n][c])







