class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n,m = len(grid),len(grid[0])
        ans = [[0]*m for _ in range(n)]
        k%=m*n
        if k == 0:
            return grid
        #print(k)
        for i in range(n):
            for j in range(m):
                singleD = i*m+j
                shifted = (singleD+k)%(m*n)
                #print(shifted)
                i_new,j_new = shifted//m,shifted%m
                #print(i_new,j_new,i,j)
                ans[i_new][j_new] = grid[i][j]
        return ans
        
               