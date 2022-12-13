class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def recursion(i,j):
            if i == len(matrix)-1:
                return matrix[i][j]
            
            val = recursion(i+1,j)
            if 0 <= j-1:
                val = min(val,recursion(i+1,j-1))
            if j+1 < len(matrix[0]):
                val = min(val,recursion(i+1,j+1))
            return val + matrix[i][j]
        ans = 10e5
        for j in range(len(matrix[0])):
            ans = min(ans,recursion(0,j))
        return ans
            
        