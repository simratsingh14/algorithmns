#User function Template for python3
from functools import lru_cache
class Solution:
    def cutRod(self, price, n):
        @lru_cache(None)
        def recursive(inx,length):
            if inx == n or length == 0:
                return 0
            if length >= inx+1:
                return max(price[inx]+recursive(inx,length-inx-1),recursive(inx+1,length))
            else:
                return recursive(inx+1,length)
        return recursive(0,n)

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