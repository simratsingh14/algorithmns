class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        count = 0
        sam = sum(arr) //3
        temp = 0
        for i in arr:
            temp += i
            if temp == sam:
                count+=1
                temp = 0
        return count >= 3
            
        