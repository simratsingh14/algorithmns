class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0,1,2] + [0]*(n-2)
        for i in range(3,n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]