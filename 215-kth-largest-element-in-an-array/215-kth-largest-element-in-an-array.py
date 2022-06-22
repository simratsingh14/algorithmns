class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        i = 0
        while len(heap) < k and i < len(nums):
            heapq.heappush(heap,nums[i])
            i+=1
        
        while i < len(nums):
            heapq.heappushpop(heap,nums[i])
            i+=1
            
        return heapq.heappop(heap)
        