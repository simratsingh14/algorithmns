class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap  = nums 
        #print(self.heap)
        for _ in range(len(self.heap)-k):
            heapq.heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if self.k > len(self.heap):
            heapq.heappush(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)