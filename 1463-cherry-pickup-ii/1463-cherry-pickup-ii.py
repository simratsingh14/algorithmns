class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def recursive(row,cola,colb):
            if not(0 <= row < len(grid) and 0 <= cola <  len(grid[0])  and 0 <= colb <  len(grid[0])):
                return -1 
            elif row == len(grid) - 1:
                ans = grid[row][cola] if cola == colb else grid[row][cola]+grid[row][colb]
                return ans
            dirs = [-1,0,1]
            ans = 0
            for da in dirs:
                for db in dirs:
                    curr = grid[row][cola] if cola == colb else grid[row][cola]+grid[row][colb]
                    ans = max(ans,curr+recursive(row+1,cola+da,colb+db))
            return ans
        return recursive(0,0,len(grid[0])-1)
        
        