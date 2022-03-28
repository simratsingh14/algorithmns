class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        distance = [[1e6+1]*len(heights[0]) for _ in range(len(heights))]
        heap = []
        distance[0][0] = 0
        
        heapq.heappush(heap,(0,0,0)) #distance,i,j
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        while heap:
            d,i,j = heapq.heappop(heap)
            for di in dirs:
                x = i + di[0]
                y = j + di[1]
                if 0 <= x < len(distance) and 0 <= y < len(distance[0]):
                    weight = max(d,abs(heights[x][y]-heights[i][j]))
                    if weight < distance[x][y]:
                        distance[x][y] = weight
                        heapq.heappush(heap,(weight,x,y))
        #print(distance)
        return distance[-1][-1]
            
        
        