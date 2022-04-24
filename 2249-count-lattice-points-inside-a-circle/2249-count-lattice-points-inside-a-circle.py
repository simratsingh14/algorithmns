class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        result = set()
        
        for circle in circles:
            x, y, r = circle
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                        result.add((i, j))
                        
        return len(result)