class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda p: (-p[0],p[1]))
        res = []
        for i in people:
            #print(res)
            res.insert(i[1],i)
        return res