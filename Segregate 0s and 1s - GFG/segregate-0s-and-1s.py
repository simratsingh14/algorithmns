#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        p1,p2 = -1,0
        while p2 < n:
            if arr[p2]:
                p2+=1
            else:
                p1+=1
                arr[p1],arr[p2] = arr[p2],arr[p1]
                p2+=1
        return arr
    
    
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# } Driver Code Ends