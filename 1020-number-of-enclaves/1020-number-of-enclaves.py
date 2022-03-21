class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r,c,grid):
            grid[r][c] = 0
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            for di in dirs:
                x = r + di[0]
                y = c + di[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
                    dfs(x,y,grid)
        for i in range(len(grid)):
            if grid[i][0]:
                dfs(i,0,grid)
            if grid[i][len(grid[0])-1]:
                dfs(i,len(grid[0])-1,grid)
        for j in range(len(grid[0])):
            if grid[0][j]:
                dfs(0,j,grid)
            if grid[len(grid)-1][j]:
                dfs(len(grid)-1,j,grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    count+=1
        return count
        
                    
        