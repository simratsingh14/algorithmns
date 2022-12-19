class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        
        def findParent(edge):
            if self.parent[edge] == edge:
                return edge
            else:
                p = findParent(self.parent[edge])
                self.parent[edge] = p
                return p
        
        def union(node1,node2):
            p1 = findParent(node1)
            p2 = findParent(node2)
            if p1 == p2:
                return 
            
            
            if self.size[p1] > self.size[p2]:
                self.size[p1] += self.size[p2]
                self.parent[p2] = self.parent[p1]
            else:
                self.size[p2] += self.size[p1]
                self.parent[p1] = self.parent[p2]
            
        for u,v in edges:
            union(u,v)
        
        #print(self.size,self.parent)
        
        return findParent(source)== findParent(destination)
        
        