class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev = 1
        candidate = nums[0]
        for i in range(1,len(nums)):
            prev += 1 if candidate == nums[i] else -1
            if prev == 0:
                candidate = nums[i]
                prev = 1
        return candidate
                
        