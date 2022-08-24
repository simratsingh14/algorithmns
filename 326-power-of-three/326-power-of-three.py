import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        ans = math.log(n,3)
        ans = round(ans,10)
        return int(ans) == ans
        