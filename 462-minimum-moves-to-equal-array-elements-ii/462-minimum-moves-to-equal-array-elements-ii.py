class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        #print(median)
        return sum([abs(i-median) for i in nums])
    
        