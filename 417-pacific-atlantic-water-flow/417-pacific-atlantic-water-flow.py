class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q = deque()
        q2 = deque()
        
        pacific =  [[False]*len(heights[0]) for _ in  range(len(heights))]
        atlantic = [[False]*len(heights[0]) for _ in  range(len(heights))]
        #print(len(pacific),len(atlantic[0]))
        n,m = len(heights),len(heights[0])
        
        for i in range(len(heights)):
            q.append((i,0))
            q2.append((i,m-1))
            #print(i,0)
            pacific[i][0] = True
            atlantic[i][m-1] = True
            
        for j in range(len(heights[0])):
            q.append((0,j))
            q2.append((n-1,j))
            pacific[0][j] = True
            atlantic[n-1][j] = True
            
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def bfs(queue,visited):
            while len(queue) != 0:
                i,j = queue.popleft()
                for d in dirs:
                    x,y = i + d[0],j + d[1]
                    if 0 <= x < len(heights) and 0 <= y < len(heights[0]) and heights[x][y] >= heights[i][j] and not visited[x][y]:
                        queue.append((x,y))
                        visited[x][y] = True
        bfs(q,pacific)
        bfs(q2,atlantic)
        ans = []
        #print(pacific,atlantic)
        for i in range(n):
            for j in range(m):
                if atlantic[i][j] and pacific[i][j]:
                    ans.append([i,j])
        return ans

                    
        
        #print(pacific,atlantic)        
                
        
                
                
        