class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lar = []
        for i in matrix:
            lar.extend(i)
        lar.sort()
        return lar[k-1]
       
        
            
        
        