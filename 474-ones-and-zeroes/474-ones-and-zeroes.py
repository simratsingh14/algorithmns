class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [(i.count('0'),i.count('1')) for i in strs]
        #print(count)
        @lru_cache(None)
        def helper(inx,m,n):
            if m == 0 and n == 0:
                return 0
            if inx == len(count):
                return 0
            if count[inx][0] <= m and count[inx][1] <= n:
                return max(1+helper(inx+1,m-count[inx][0],n-count[inx][1]),helper(inx+1,m,n))
            else:
                return helper(inx+1,m,n)
        return 0 if helper(0,m,n) == -100 else helper(0,m,n)