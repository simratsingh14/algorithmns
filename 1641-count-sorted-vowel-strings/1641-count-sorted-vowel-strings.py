class Solution:
    def countVowelStrings(self, n: int) -> int:
        def helper(inx,l):
            if l == n:
                return 1
            if inx == 5:
                return 0
            ans = 0
            for i in range(inx,5):
                ans+=helper(i,l+1)
            return ans
        return helper(0,0)
                
        