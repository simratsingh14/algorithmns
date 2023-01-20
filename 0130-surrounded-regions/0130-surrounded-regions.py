class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j):
            grid[i][j] = 'A'
            
            for d in dirs:
                x,y = i+d[0],j+d[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 'O':
                    dfs(x,y)
                    
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i in (0,len(grid)-1) or j in (0,len(grid[0])-1)) and grid[i][j] == 'O':
                    #print(i,j)
                    dfs(i,j)
                    
        #print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == 'A':
                    grid[i][j] = 'O'
        
                    
            
            
        