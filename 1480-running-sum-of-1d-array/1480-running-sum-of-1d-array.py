class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = 0
        arr = []
        for i in nums:
            ans+=i
            arr.append(ans)
        return arr