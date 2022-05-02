class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left,right = 0,len(nums)-1
        ans = [0]*len(nums)
        for i in nums:
            if i % 2 == 0:
                ans[left] = i
                left+=1
            else:
                ans[right] = i
                right-=1
        return ans
        