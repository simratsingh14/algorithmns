class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            val = nums2.index(i)
            while val < len(nums2) and nums2[val] <= i:
                val+=1
            if val == len(nums2):
                ans.append(-1)
            else:
                ans.append(nums2[val])
        return ans
        