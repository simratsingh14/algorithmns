'''
Given two strings X and Y, print the shortest string that has both X and Y as subsequences. If multiple shortest supersequence exists, 
print any one of them.
'''

x = 'AGGTAB'
y = 'GXTXAYB'

def lcsPrint(x,y):
    m,n = len(x),len(y)
    dp = [[''] + [None]*(n) for i in range(m+1)]
    dp[0] = ['']*(n+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                dp[i][j]= dp[i-1][j-1] + x[i-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],key=lambda x:len(x))
    # print(dp)
    ans = ''
    i,j = m,n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            ans += x[i-1]
            i-=1
            j-=1
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                ans += x[i-1]
                i-=1
            else:
                ans += y[j-1]
                j-=1
    while i > 0:
        ans+= x[i-1]
        i-=1
    while j > 0:
        ans+= y[j-1]
        j-=1
                
    return (ans)[::-1]



print(lcsPrint(x,y))

 