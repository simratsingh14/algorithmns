class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def LCS(s,t):
            n,m = len(s),len(t)
            prev,curr = [0]*(n+1),[0]*(n+1)
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s[j-1] == t[i-1]:
                        curr[j] = 1 + prev[j-1]
                    else:
                        curr[j] = max(curr[j-1],prev[j])
                prev = curr[:]
            return prev[-1]
        return LCS(s,s[::-1])
            
        