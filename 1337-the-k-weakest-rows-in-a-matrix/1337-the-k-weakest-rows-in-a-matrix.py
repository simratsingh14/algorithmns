class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            s = sum(mat[i])
            heapq.heappush(heap,(s,i))
        #print(heap)
        arr = []
        for i in range(k):
            arr.append(heapq.heappop(heap)[1])
        return arr
                    
        