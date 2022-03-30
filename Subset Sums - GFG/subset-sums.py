#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		self.ans = []
		def subset(inx,total = 0):
		    if inx  == len(arr):
		        self.ans.append(total)
		        return
		    subset(inx+1,total)
		    subset(inx+1,total+arr[inx])
	    subset(0)
	    return self.ans
		  
		    
		    
		        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends