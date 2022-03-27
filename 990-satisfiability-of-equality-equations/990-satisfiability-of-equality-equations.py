class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.parent = [i for i in range(26)]
        self.size = [1]*26
        def findParent(edge):
            if self.parent[edge] == edge:
                return edge
            par = self.parent[edge]
            ans = findParent(par)
            self.parent[edge] = ans
            return ans
        for i in equations:
            if i[1] == '=':   
                pu = findParent(ord(i[0]) - ord('a'))
                pv = findParent(ord(i[3]) - ord('a'))
                if self.size[pu] > self.size[pv]:
                    self.size[pu] += self.size[pv]
                    self.parent[pv] = pu
                else:
                    self.size[pv] += self.size[pu]
                    self.parent[pu] = pv
        for i in equations:
            if i[1] == '!':
                pu = findParent(ord(i[0]) - ord('a'))
                pv = findParent(ord(i[3]) - ord('a'))
                if pu == pv:
                    return False
        return True

                
    
                