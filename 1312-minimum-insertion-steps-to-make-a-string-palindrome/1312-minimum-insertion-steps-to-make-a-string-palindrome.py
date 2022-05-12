class Solution:
    def minInsertions(self, s: str) -> int:
        if s[::-1] == s:
            return 0
        rev = s[::-1]
        prev = [0]*(len(s)+1)
        curr = [0]*(len(s)+1)
        for i in range(1,len(prev)):
            for j in range(1,len(curr)):
                if s[i-1] == rev[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr[:]
        return len(s)-prev[-1] 
        