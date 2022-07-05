class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = Counter(nums)
        size = 0
        for i in ans.keys():
            if ans[i-1] ==0:
                k = i+1
                s = 1
                while ans[k]>0:
                    k+=1
                    s+=1
                #print(s,k)
                size = max(size,s)
        return size
                
        