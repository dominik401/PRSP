

def solve(n,m,k):
    dp = [[0] * m for _ in range(n)] # inicijalizacija polja

    dp [0][0] = 0 #početna pozicija

    for j in range(1, m): # pomicanje desno
        dp[0][j] = dp[0][j-1] + 1
    
    for i in range(1, n): # pomicanje dolje
        dp[i][0] = dp[i-1][0]+1
    
    for i in range(1, n): # ostatak mreže
        for j in range(1,m):
            dp[i][j] = min(dp[i-1][j] + j + 1, dp[i][j-i] + i + 1)
    return dp[n - 1][m - 1] == k

t = int(input()) # broj testnih slučajeva

for _ in range(t): 
    n, m, k = map(int, input().split()) # ulazne vrijednosti dimenzija mxn i k burla

    if solve(n,m,k):
        print("YES")
    else:
        print("NO")