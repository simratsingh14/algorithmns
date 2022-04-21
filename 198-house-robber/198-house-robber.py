class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(inx):
            if inx >= len(nums):
                return 0
            return max(nums[inx] + helper(inx+2),helper(inx+1))
        return helper(0)
            
            
        