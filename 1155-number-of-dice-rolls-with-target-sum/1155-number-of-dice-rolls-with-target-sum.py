from functools import cache
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def recur(d, current):
            if d == n:
                return current == target
            s = sum([recur(d+1, current+i) for i in range(1,k+1)])
            return s
        return recur(0,0) % int(10**9 + 7)