class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        left,right = 0 ,len(people) - 1
        while left <= right:
           # print(people[left],people[right])
            if people[left] + people[right] <= limit:
                left+=1
            right-=1
            count+=1
        return count
            
        
        