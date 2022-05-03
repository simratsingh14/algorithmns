class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        total = sum(nums)//2
        dp = [True] + [False]*total
        #print(dp)
        for i in nums:
            #print(dp)
            for j in range(len(dp)-1,0,-1):
                if j >= i:
                    dp[j] = dp[j-i] or dp[j]
        #print(dp)
        return dp[-1]
                
        