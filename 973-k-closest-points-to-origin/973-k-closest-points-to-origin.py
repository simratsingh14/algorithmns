class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = x**2+y**2
            if len(heap) < k:
                heapq.heappush(heap,(-1*dist,x,y))
            else:
                heapq.heappushpop(heap,(-1*dist,x,y))
        #print(heap)
        return [[i[1],i[2]] for i in heap]
                