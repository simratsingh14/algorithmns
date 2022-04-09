class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.parent = [i for i in range(len(isConnected))]
        self.size = [1]*len(isConnected)
        def findParent(node):
            if self.parent[node] == node:
                return node
            val = self.parent[node]
            self.parent[node] = findParent(val)
            return self.parent[val]
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    pu,pv = findParent(i),findParent(j)
                    if self.size[pu] > self.size[pv]:
                        self.size[pu] += self.size[pv]
                        self.parent[pv] = self.parent[pu]
                    else:
                        self.size[pv] += self.size[pu]
                        self.parent[pu] = self.parent[pv]
        ans = 0
        for idx,val in enumerate(self.parent):
            if val == idx:
                ans+=1
        return ans
            
                        
        