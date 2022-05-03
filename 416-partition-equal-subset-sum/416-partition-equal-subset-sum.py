class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        total = sum(nums)//2
        dp = [[True] + [False]*total for _ in range(len(nums)+1)]
        #print(dp)
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        #print(dp)
        return dp[-1][-1]
                
        