#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		dp1 = [1]*len(nums)
		for i in range(1,len(nums)):
		    for j in range(i):
		        if nums[j] < nums[i]:
		            dp1[i] = max(dp1[i],1+dp1[j])
		dp2 = [1]*len(nums)
		for i in range(len(nums)-2,-1,-1):
		    for j in range(len(nums)-1,i,-1):
		        if nums[j] < nums[i]:
		            dp2[i] = max(dp2[i],1+dp2[j])
		#print(dp1,dp2)
		ans = 0
		for i in range(len(nums)):
		    ans = max(ans,dp1[i]+dp2[i])
		return ans-1
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends