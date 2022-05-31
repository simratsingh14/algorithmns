class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            prev = ans[-1]
            temp = [1]
            for j in range(1,len(prev)):
                temp.append(prev[j]+prev[j-1])
            temp.append(1)
            ans.append(temp)
        return ans
                
            
        