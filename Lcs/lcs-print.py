'''
Given two sequences, print the longest subsequence present in both of them.
Example:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3. 
'''
x = 'acbcf'
y = 'abcdaf'
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
    return dp[-1][-1]


print(lcsPrint(x,y))

