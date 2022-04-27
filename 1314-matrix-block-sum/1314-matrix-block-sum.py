class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        self.sumMat = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.sumMat[i][j] = self.sumMat[i-1][j] + self.sumMat[i][j-1] + mat[i-1][j-1] - self.sumMat[i-1][j-1]
        def query(r1,c1,r2,c2):
            a = self.sumMat[r1][c1]
            b = self.sumMat[r1][c2+1]
            c = self.sumMat[r2+1][c1]
            d = self.sumMat[r2+1][c2+1]
            return a + d -(b + c)
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1,r2,c1,c2  = max(0,i-k),min(m-1,i+k),max(0,j-k),min(n-1,j+k)
                ans[i][j] = query(r1,c1,r2,c2)
        return ans