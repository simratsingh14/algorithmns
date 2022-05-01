class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            ans = []
            for i in s:
                if i == '#' and len(ans) != 0:
                    ans.pop()
                elif i != '#':
                    ans.append(i)
            return ''.join(ans)
        return build(s) == build(t)
                    
        
        