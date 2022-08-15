class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def GreaterElementRight(nums):
            n = len(nums)
            stack = [n]
            ans = [0]*(n-1) + [n]
            for i in range(len(nums)-1,-1,-1):
                while stack[-1] != n and len(stack)!=0 and nums[stack[-1]] < nums[i]:
                    stack.pop()
                if len(stack) == 0 or stack[-1] == n:
                    ans[i] = n
                else:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans
        arr = GreaterElementRight(nums)
        ans = []
        idx = 0
        for i in range(len(nums)-k+1):
            si = i
            ei = i + k -1
            if idx<si:
                idx = si
            while idx!=len(nums) and arr[idx] <= ei:
                idx = arr[idx]
            if idx == len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[idx])
        return ans
            
        