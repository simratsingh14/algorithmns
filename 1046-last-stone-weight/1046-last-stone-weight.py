class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for  i in stones:
            heapq.heappush(heap,-1*i)
        while len(heap) > 1:
            x = -1*heapq.heappop(heap)
            y = -1*heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,y-x)
        if len(heap) == 0:
            return 0
        else:
            return -1*heap[0]
        
        