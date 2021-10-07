'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.
Input: s = "rabbbit", t = "rabbit"
Output: 3
'''
s = "rabbbit" 
t = "rabbit"
def numDistinct(s,t):
    dp = [[1] + [0]*(len(s)) for i in len(t)+1]
    