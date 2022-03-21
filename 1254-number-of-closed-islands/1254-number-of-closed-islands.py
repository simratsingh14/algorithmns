class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row,col):
            grid[row][col] = 1
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            for d in dirs:
                x = row + d[0]
                y = col + d[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y]:
                    dfs(x,y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1) and grid[i][j]==0:
                    dfs(i,j)
        # for i in grid:
        #     print(i)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    dfs(i,j)
                    count+=1
       
        
        return count
        