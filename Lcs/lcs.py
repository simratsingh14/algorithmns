"""
Longest Common Subsequence Problem solution using Memoization
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

For example, “abc”,  “abg”, “bdf”, “aeg”,  ‘”acefg”, .. etc are subsequences of “abcdefg”.

"""

str1 = "ABCDGH"
str2 = "AEDFHR"


def lcsRecursive(str1,str2):
    if str1 == '' or str2 == '':
        return 0
    else:
        if str2[-1] == str1[-1]:
            return 1 + lcsRecursive(str1[:-1],str2[:-1])
        else:
            return max(lcsRecursive(str1,str2[:-1]),lcsRecursive(str1[:-1],str2))

print(lcsRecursive(str1,str2))


def lcsBottomUp(str1,str2):
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

print(lcsBottomUp(str1,str2))


