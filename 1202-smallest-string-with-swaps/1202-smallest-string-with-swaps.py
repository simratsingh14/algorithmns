class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = [i for i in range(len(s))]
        self.size = [1]*len(s)
        
        def findParent(node):
            if self.parent[node] != node:
                self.parent[node] = findParent(self.parent[node])
            return self.parent[node]
        def union(pairs):
            for i in pairs:
                x,y = i[0],i[1]
                pu,pv = findParent(x),findParent(y)
                if self.size[pu] > self.size[pv]:
                    self.size[pu] += self.size[pv]
                    self.parent[pv] = self.parent[pu]
                else:
                    self.size[pv] += self.size[pu]
                    self.parent[pu] = pv
        union(pairs)
        #print(self.parent)
        
        groups = defaultdict(list)
        for i,val in enumerate(s):
            groups[findParent(i)]+=val
        for idx,val in groups.items():
            groups[idx].sort(reverse = True)    
        #print(groups)
        
        ans = []
        for i in self.parent:
            ans.append(groups[i].pop())
        return ''.join(ans)
            
            
    