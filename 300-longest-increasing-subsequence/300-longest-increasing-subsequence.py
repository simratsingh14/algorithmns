class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr  = []
        for i in nums:
            #print(arr)
            inx = bisect_left(arr,i)
            if inx == len(arr):
                arr.append(i)
            else:
                arr[inx] = i
        return len(arr)
        