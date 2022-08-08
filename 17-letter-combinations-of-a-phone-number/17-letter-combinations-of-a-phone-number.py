class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        prev = ['']
        if len(digits) == 0:
            return []
        for i in range(len(digits)):
            ans = []
            
            s = d[int(digits[i])]
            for i in prev:
                for j in s:
                    ans.append(i+j)
            prev = ans[:]
            ans = []
        
        return prev
            
        