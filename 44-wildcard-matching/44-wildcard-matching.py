class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def helper(l1,l2):
            if l1 == len(s) and l2 == len(p):
                return True
            elif len(p) == l2:
                return False
            elif len(s) == l1 and p[l2] != '*':
                return False
            
            if p[l2] == '*':
                if len(s) == l1:
                    return helper(l1,l2+1)
                return helper(l1+1,l2) or helper(l1+1,l2+1) or helper(l1,l2+1)
            elif p[l2] == '?':
                return helper(l1+1,l2+1)
            else:
                return s[l1] == p[l2] and helper(l1+1,l2+1)
        return helper(0,0)
            
        