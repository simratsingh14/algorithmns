#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		
		bits = 1
		s = 0
		for i in arr:
		    bits |= bits << i
		    s+=i
		 
		if s&1:
		    left,right = s//2,s//2+1
		else:
		    left,right = s//2,s//2
		   
		while  bits>>left&1 == 0 or bits>>right&1 == 0:
		    #print(left,right)
		    left-=1
		    right+=1
		return right-left
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends