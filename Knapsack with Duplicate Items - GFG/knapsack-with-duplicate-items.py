#User function Template for python3
from functools import lru_cache
class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0]*(W+1)
        
        for i in range(len(wt)):
            for j in range(1,len(dp)):
                if j >= wt[i]:
                    dp[j] = max(val[i]+dp[j-wt[i]],dp[j])
        #(dp)           
        return dp[-1]
                
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends