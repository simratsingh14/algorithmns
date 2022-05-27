class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = -1
        if num == 0:
            return 0
        while num!=0:
            if num&1:
                count+=1
            count+=1
            num = num >>1
        return count
        