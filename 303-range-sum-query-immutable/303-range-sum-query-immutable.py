class NumArray:

    def __init__(self, nums: List[int]):
        self.range = [0]
        for i in range(1,len(nums)+1):
            self.range.append(nums[i-1] + self.range[i-1])
        #print(self.range)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.range[right+1] - self.range[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)