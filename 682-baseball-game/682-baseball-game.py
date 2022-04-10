class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for i in ops:
            if i == '+':
                arr.append(arr[-1] + arr[-2])
            elif i == 'D':
                arr.append(arr[-1]*2)
            elif i == 'C':
                arr.pop()
            else:
                arr.append(int(i))
        return sum(arr)