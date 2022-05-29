class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        choice,ans = 0,0
        for i in nums:
            choice = max(0,choice+i)
            ans = max(ans,choice)
        return max(nums) if ans == 0 else ans 