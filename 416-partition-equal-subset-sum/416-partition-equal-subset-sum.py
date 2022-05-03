class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        total = sum(nums)//2
        dp = 1                #[True] + [False]*total
        #print(dp)
        for i in nums:
            #dp[j] = dp[j-i] or dp[j]
            dp |= dp << i
        
        return (dp >> total) & 1 == 1
                
        