class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1]*len(nums)
        inx = [i for i in range(len(nums))]
        max_inx,max_val = 0,1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    #print(nums[i],nums[j])
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1+dp[j]
                        inx[i] = j
            if dp[i] > max_val:
                max_val = dp[i]
                max_inx = i
        ans = []
        while True:
            if max_inx == inx[max_inx]:
                break
            ans.append(nums[max_inx])
            max_inx = inx[max_inx]
        ans.append(nums[max_inx])
            
        #print(dp,inx,max_inx)
        return ans
        