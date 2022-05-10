class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.arr = []
        def recursion(num,ssf,temp):
            if ssf == n and len(temp) == k :
                self.arr.append(temp)
                return 
            if len(temp) > k or ssf > n or num == 10:
                return 
            if ssf + num <= n:
                recursion(num+1,ssf+num,temp+[num])
            recursion(num+1,ssf,temp)
        recursion(1,0,[])
        return self.arr
                
                
     