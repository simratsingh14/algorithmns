class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = defaultdict(list)
        for idx,val in enumerate(manager):
            d[val].append(idx)
        def dfs(source):
            if not d[source]:
                return 0
            ans = 0 
            for i in d[source]:
                ans = max(informTime[source] + dfs(i),ans)
            return ans
        return dfs(headID)
            
            
        