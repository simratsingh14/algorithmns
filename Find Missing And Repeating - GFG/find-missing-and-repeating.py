#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        sum_arr = sum(arr)   # X is extra number and Y is missing
        sum_num = n*(n+1)//2
        X_Y = sum_arr-sum_num # X-Y  
        sum_arr2 = sum([i**2 for i in arr])
        sum_num2 = sum_num*(2*n+1)//3
        sq_diff = sum_arr2-sum_num2            # X*2-Y*2
        sumXY = sq_diff//X_Y
        X = (sumXY + X_Y)//2
        Y = (sumXY - X_Y)//2
        return [X,Y]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends