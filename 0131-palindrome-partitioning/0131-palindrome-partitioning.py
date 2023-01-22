class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        
        def isPallindrome(s):
            return s == s[::-1]
        
        def helper(start = 0,curr = 1,temp = []):
            #print(start,curr,s[start:curr])
            if curr == len(s):
                if isPallindrome(s[start:curr]):
                    self.ans.append(temp+ [s[start:curr]])
                    return
                return
            if isPallindrome(s[start:curr]):
                helper(curr,curr+1,temp+[s[start:curr]])
            helper(start,curr+1,temp)
        helper()
        return self.ans
                
                
                