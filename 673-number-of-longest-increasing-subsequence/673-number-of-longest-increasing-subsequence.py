class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        count = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j]+1:
                        count[i]+= count[j]
                    elif dp[i] < dp[j]+1:
                        count[i] = count[j]
                        dp[i] = dp[j]+1
        maxvalue = max(dp)
        #print(dp,count,maxvalue)
        ans = 0
        for i in range(len(dp)):
            if dp[i] == maxvalue:
                ans += count[i]
        return ans
      
        
        