class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(len(edges)+1)]
        self.size = [0] + [1]*(len(edges)+1)
        def findParent(edge):
            if self.parent[edge] == edge:
                return edge
            lu = self.parent[edge]
            elem = findParent(lu)
            self.parent[edge] = elem
            return elem
        
        for i in edges:
            #print(self.parent,self.size,i)
            pu = findParent(i[0])
            pv = findParent(i[1])
            #print(pu,pv)
            if pu == pv:
                return i
            if self.size[pu] >= self.size[pv]:   # Making parent as u
                self.size[pu] += self.size[pv]
                self.parent[pv] = pu
            else:
                self.size[pv] += self.size[pu]
                self.parent[pu] = pv
            