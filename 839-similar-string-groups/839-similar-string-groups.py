class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        self.parent = [i for i in range(len(strs))]
        self.size = [1]*len(strs)
        
        def isSimilar(str1,str2):
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count+=1
            if count <= 2:
                return True
            return False
        
        pairs = []
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if isSimilar(strs[i],strs[j]):
                    pairs.append((i,j))
        
        def findParent(node):
            if self.parent[node] == node:
                return node
            self.parent[node] = findParent(self.parent[node])
            return self.parent[node]
        
        for x,y in pairs:
            pu,pv = findParent(x),findParent(y)
            if self.size[pu] > self.size[pv]:
                self.size[pu]+=self.size[pv]
                self.parent[pv] = pu
            else:
                self.size[pv]+=self.size[pu]
                self.parent[pu] = pv
                
        numberOfGroup = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                numberOfGroup+=1
        return numberOfGroup
        
                
                    
            