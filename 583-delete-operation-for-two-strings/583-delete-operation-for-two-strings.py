class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def lcs(word1,word2):
            n,m = len(word1),len(word2)
            prev,curr = [0]*(n+1),[0]*(n+1)
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if word1[j-1] == word2[i-1]:
                        curr[j] = 1 + prev[j-1]
                    else:
                        curr[j] = max(curr[j-1],prev[j])
                prev = curr[:]
            return prev[-1]
        return len(word1) + len(word2) -2*lcs(word1,word2)
        
                        
                        
                
        