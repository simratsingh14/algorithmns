class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort,hare = nums[0],nums[0]
        while True:
            #print(nums[tort],nums[hare])
            tort = nums[tort]
            hare = nums[nums[hare]]
            if tort == hare:
                break
        tort = nums[0]
        while tort != hare:
            tort = nums[tort]
            hare = nums[hare]
        return hare
            
        
        
        