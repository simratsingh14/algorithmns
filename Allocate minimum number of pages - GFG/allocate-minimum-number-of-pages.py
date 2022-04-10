class Solution:
    def findPages(self,A, N, M):
        def isValid(A,M,mid):
            student = 1 
            sam = 0
            for i in A:
                sam+= i
                if sam > mid:
                    sam = i
                    student+=1
                if student > M:
                    return False
            return True
        
        if N < M:
            return -1
        low = max(A)
        high = sum(A)
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if isValid(A,M,mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends