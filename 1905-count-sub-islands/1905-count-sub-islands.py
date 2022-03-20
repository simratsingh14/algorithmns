class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid1,grid2,i,j):
            ans = grid1[i][j] == grid2[i][j]
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            grid2[i][j] = 0
            for di in dirs:
                x  = i + di[0]
                y = j + di[1]
                if 0 <= x < len(grid1) and 0 <= y < len(grid1[0]) and grid2[x][y]==1:
                    ans = dfs(grid1,grid2,x,y) and ans
            return ans
        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    if dfs(grid1,grid2,i,j):
                        count+=1
        return count
    
        
                    
            
        