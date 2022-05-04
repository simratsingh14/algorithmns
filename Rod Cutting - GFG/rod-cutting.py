#User function Template for python3
from functools import lru_cache
class Solution:
    def cutRod(self, price, n):
        dp = [[0]*(n+1) for i in range(n+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j >= i:
                    dp[i][j] = max(dp[i-1][j],price[i-1]+dp[i][j-i])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends