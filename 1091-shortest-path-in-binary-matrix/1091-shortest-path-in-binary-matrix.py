class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q  = deque()
        if grid[0][0]:
            return -1
        q.append((0,0))
        if len(grid) - 1 == 0:
            return 1
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        level = 1
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for di in dirs:
                    x,y = i + di[0],j+di[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y]:
                        #print(x,y)
                        grid[x][y] = 1
                        if x == len(grid) - 1 and y  == len(grid[0]) - 1:
                            return level +1
                        q.append((x,y))
            level+=1
        return -1
        