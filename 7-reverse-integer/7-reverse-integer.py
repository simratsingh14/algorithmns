class Solution:
    def reverse(self, x: int) -> int:
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff
        
        if x >= 0:
            x = int(str(x)[::-1])
        
        else:
            a = str(x)[1::]
            x = -1*int(a[::-1])
            
        if x>=0:
            if x & pos_limit == x:
                return x
            else:
                return 0
        else:
            if x & neg_limit == neg_limit:
                return x
            else:
                return 0