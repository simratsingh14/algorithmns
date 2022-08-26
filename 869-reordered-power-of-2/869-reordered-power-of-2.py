class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = [Counter(str(1<<i)) for i in range(31)]
        return Counter(str(n)) in arr
        