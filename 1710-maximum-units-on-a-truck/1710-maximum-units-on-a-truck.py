class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for i in boxTypes:
            heapq.heappush(heap,(-i[1],i[0]))
        #print(heap)
        ans = 0
        while len(heap) > 0 and truckSize > 0:
            box,cap = heapq.heappop(heap)
            cap = min(truckSize,cap)
            ans += -1*box*cap
            truckSize-=cap
        return ans
            
        