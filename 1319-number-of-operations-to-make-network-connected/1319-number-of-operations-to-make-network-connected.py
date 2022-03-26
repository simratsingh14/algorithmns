class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        
        def findParent(edge):
            if self.parent[edge] == edge:
                return edge
            temp = self.parent[edge]
            ans = findParent(temp)
            self.parent[edge] = ans
            return ans
        
        redundant = 0
        for i in connections:
            pu = findParent(i[0])
            pv = findParent(i[1])
            #print(self.parent,self.size,i,pu,pv)
            if pu == pv:
                redundant = redundant + 1
            elif self.size[pu] > self.size[pv]:
                self.size[pu] += self.size[pv]
                self.parent[pv] = pu
            else:
                self.size[pv] += self.size[pu]
                self.parent[pu] = pv
        #print(redundant)
        #print(self.parent)
        for i in range(len(self.parent)):
            self.parent[i] = findParent(i)
        group = len(set(self.parent))  
        if group - 1 <= redundant:
            return group -1
        else:
            return -1
            
                
            
        