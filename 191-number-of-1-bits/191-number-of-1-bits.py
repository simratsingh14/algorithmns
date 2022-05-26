class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n!=0:
            mask = n & (-n)
            n = n - mask
            count+=1
        return count