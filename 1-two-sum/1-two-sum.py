class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = Counter(nums)
        ans = 0
        for i in d:
            #print(i,d[i])
            if 2*i == target and d[i] >1:
                ans = i
                break
            elif 2*i != target and d[target-i] >= 1:
                ans = i
                break
        elem1 = nums.index(ans)
        elem2 = nums.index(target-ans,elem1+1)
                
        return [elem1,elem2]
        
                
                
        