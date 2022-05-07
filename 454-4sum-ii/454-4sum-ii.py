class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        da = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                sa = nums1[i]+nums2[j]
                da[sa]+= 1 
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                b = nums3[i] + nums4[j]
                if da[0-b] > 0:
                    count+=da[0-b]
        return count
    
            
            
        