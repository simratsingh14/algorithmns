class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            val = 1
            for j in range(i):
                if nums[i] > nums[j] and  dp[i] < dp[i]+dp[j]:
                    val = max(val,dp[i]+dp[j])
            dp[i] = val 
        #print(dp)
        return max(dp)