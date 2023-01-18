class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans,curr,total,ans2,curr2 = nums[0],0,0,nums[0],0
        for i in nums:
            curr = max(i,curr+i)
            ans = max(curr,ans)
            curr2 = min(i,curr2+i)
            ans2 = min(curr2,ans2) 
            total += i
        if ans <= 0:
            return max(nums)
        #print(ans2)
        return max(ans,total - ans2)
            
        