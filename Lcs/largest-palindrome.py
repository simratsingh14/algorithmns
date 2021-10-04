"""
Longest Palindromic Subsequence
Given a sequence, find the length of the longest palindromic subsequence in it.
Example :
Input:"bbbab"
Output:4
"""

X = 'bbbab'
def lcsPallindrome(str1,str2):
    m,n = len(str1),len(str2)
    dp = [[0] +[-1]*(n) for i in range(m+1)]
    dp[0] = [0]*(n+1)
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    # print(dp)
    return dp[-1][-1]

print(lcsPallindrome(X,X[::-1]))

