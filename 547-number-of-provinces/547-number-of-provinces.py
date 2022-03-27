class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.parent = [i for i in range(len(isConnected))]
        self.size = [1]*len(isConnected)
        
        def findParent(edge):
            if self.parent[edge] == edge:
                return edge
            
            par = self.parent[edge]
            ans = findParent(par)
            self.parent[edge] = ans
            return ans
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j]:
                    pu = findParent(i)
                    pv = findParent(j)
                    if self.size[pu] > self.size[pv]:
                        self.size[pu]+=self.size[pv]
                        self.parent[pv] = pu
                    else:
                        self.size[pv]+=self.size[pu]
                        self.parent[pu] = pv
        count = 0            
        for idx,val in enumerate(self.parent):
            if idx == val:
                count+=1
        return count
            