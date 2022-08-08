class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.arr = []
        def generate(left=n,right=n,ans = ''):
            #print(left,right,ans)
            if left == 0 and right == 0:
                self.arr.append(ans)
                return
            elif left == 0:
                generate(left,right-1,ans+')')
                return
            elif right == 0:
                return
            if right-1 >= left:
                generate(left,right-1,ans+')')
            generate(left-1,right,ans+'(')
        generate()
        return self.arr
            
                
                
            
            
            
        