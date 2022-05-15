class Solution:
	def minimumMountainRemovals(self, nums: List[int]) -> int:
		dp1 = [0]*len(nums)
		for i in range(1,len(nums)):
			for j in range(i):
				if nums[j] < nums[i]:
					dp1[i] = max(dp1[i],1+dp1[j])
					
		dp2 = [0]*len(nums)
		for i in range(len(nums)-2,-1,-1):
			for j in range(len(nums)-1,i,-1):
				if nums[j] < nums[i]:
					dp2[i] = max(dp2[i],1+dp2[j])
		#print(dp1,dp2)
		ans = 0
		for i in range(len(nums)):
			if dp1[i]*dp2[i] != 0:
				ans = max(ans,dp1[i]+dp2[i])
		return len(nums)-ans-1
		