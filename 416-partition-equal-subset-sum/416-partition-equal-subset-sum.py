class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        @lru_cache(None)
        def recursive(inx,val):
            if val < 0:
                return False
            elif val != 0 and inx == len(nums):
                return False
            elif val == 0:
                return True
            return recursive(inx+1,val) or recursive(inx+1,val-nums[inx])
        return recursive(0,sum(nums)//2)
        