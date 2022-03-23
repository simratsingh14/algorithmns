class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    q.append((i,j))
        level = 0
        ans = -1
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while  q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for di in dirs:
                    x,y = i + di[0],j + di[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y]:
                        q.append((x,y))
                        ans = max(ans,level+1)
                        grid[x][y] = 1
            level+=1
        return ans
                
        