#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		dp = [1] + [0]*sum
		mod  = 1000000007
		for i in arr:
		    #print(dp)
		    for j in range(sum,-1,-1):
		        if j >= i:
		            dp[j] += dp[j-i]
		#print(dp)
		return int(dp[-1]%mod)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends