class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def subset(inx,temp= []):
            if inx == len(nums):
                if sorted(temp) not in self.ans:
                    self.ans.append(sorted(temp))
                return
            subset(inx+1,temp)
            subset(inx+1,temp+[nums[inx]])
            
        subset(0)
        return self.ans
            
                    
        