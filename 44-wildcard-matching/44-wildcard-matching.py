class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def helper(l1,l2):
            if l1 == 0 and l2 == 0:
                return True
            elif l2 == 0:
                return False
            elif l1 == 0 and p[l2-1] != '*':
                return False
            
            if p[l2-1] == '*':
                if l1 == 0:
                    return helper(l1,l2-1)
                return helper(l1-1,l2) or helper(l1-1,l2-1) or helper(l1,l2-1)
            elif p[l2-1] == '?':
                return helper(l1-1,l2-1)
            else:
                return s[l1-1] == p[l2-1] and helper(l1-1,l2-1)
        return helper(len(s),len(p))
            
            
        