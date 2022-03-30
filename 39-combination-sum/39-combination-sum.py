class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def csum(inx,arr,target):
            if target == 0:
                self.ans.append(arr)
                return
            elif target < 0 or inx == len(candidates):
                return
            csum(inx,arr+[candidates[inx]],target-candidates[inx])
            csum(inx+1,arr,target)
            
        csum(0,[],target)
        return self.ans