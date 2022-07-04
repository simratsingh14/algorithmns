class Solution:
    def candy(self, r: List[int]) -> int:
        ans = [1]*len(r)
        for i in range(len(r)-1):
            if r[i] < r[i+1]:
                ans[i+1] = max(1+ans[i],ans[i+1])
        for i in range(len(r)-2,-1,-1):
            if r[i+1] < r[i]:
                ans[i] = max(1 + ans[i+1],ans[i])
        return sum(ans)
        