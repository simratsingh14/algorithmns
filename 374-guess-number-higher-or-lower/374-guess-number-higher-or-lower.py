class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        mid = (1+ n)//2
        low,high = 1,n
        while guess(mid) != 0:
            if guess(mid) > 0:
                low = mid
            elif guess(mid) < 0:
                high = mid
            mid = (high + low)//2
        return mid
            