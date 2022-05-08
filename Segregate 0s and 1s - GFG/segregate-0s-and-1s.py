#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        left,right = 0,n-1
        while left < right:
            if arr[left]:
                arr[left],arr[right] = arr[right],arr[left]
                right-=1
            else:
                left+=1
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