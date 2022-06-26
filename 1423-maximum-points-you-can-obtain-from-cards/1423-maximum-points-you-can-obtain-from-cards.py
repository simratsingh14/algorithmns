class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cumaltativeSum = [0]
        count = 0
        for i in cardPoints:
            count+=i
            cumaltativeSum.append(count)
        count = 0  
        backsum = [0]
        for i in cardPoints[::-1]:
            count+=i
            backsum.append(count)
        final = [cumaltativeSum[i] + backsum[k-i] for i in range(k+1)]
        #print(cumaltativeSum,backsum,final)
        return max(final)
            
            
            
        
            
        