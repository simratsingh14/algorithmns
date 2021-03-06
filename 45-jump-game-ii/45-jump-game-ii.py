class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10001]*len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            #print(dp)
            minVal = 10001
            if nums[i] == 0:
                continue
            for jump in range(nums[i]+1):
                if i+jump < len(nums):
                    minVal = min(minVal,1+dp[i+jump])
                else:
                    break
            dp[i] = minVal
        #print(dp)
        return dp[0]
        
        