class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = (sum(nums)-target)
        if target&1:
            return 0
        else:
            target = target//2
        if target < 0:
            return 0
        dp = [1] + [0]*target
        for i in nums:
            for j in range(target,-1,-1):
                if j >= i:
                    dp[j] += dp[j-i]
        print(dp)
        print(sum(nums))
        return dp[-1]
        