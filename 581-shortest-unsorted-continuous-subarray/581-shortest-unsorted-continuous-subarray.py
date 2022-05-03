class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = -1
        last = -1
        ans = sorted(nums)
        for i in range(len(nums)):
            if ans[i] != nums[i]:
                if start == -1:
                    start = i
                last = i 
            
        #print(nums)
        #print(ans)
        if start == -1:
            return 0
        return last  - start +1
        