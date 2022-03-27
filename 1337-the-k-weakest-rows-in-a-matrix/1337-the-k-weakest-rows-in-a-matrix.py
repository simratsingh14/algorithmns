class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        def findSoldier(arr):
            left,right = 0,len(arr)-1
            while left  <= right:
                mid = left + (right-left)//2
                if arr[mid]:
                    left = mid+1
                else:
                    right = mid-1
            return left
        for i in range(len(mat)):
            s = findSoldier(mat[i])
            heapq.heappush(heap,(s,i))
        #print(heap)
        arr = []
        for i in range(k):
            arr.append(heapq.heappop(heap)[1])
        return arr
                    
        