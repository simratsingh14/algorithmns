from functools import lru_cache
import math

def numSquares(n: int) -> int:
        ps = []
        i = 1
        while i * i <= n:
            ps.append(i * i)
            i += 1

        @lru_cache(None)
        def dp(target):
            if target == 0:
                return 0

            ans = math.inf
            for num in ps:
                if target >= num:
                    ans = min(ans, dp(target - num) + 1)
            return ans

        return dp(n)

print(numSquares(40))