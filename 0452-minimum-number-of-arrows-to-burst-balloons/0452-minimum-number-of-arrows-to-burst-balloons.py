class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort(key = lambda x:x[1])
        curr = points[0][1]
        ans = 1
        for i in range(1,len(points)):
            if curr >= points[i][0]:
                continue
            else:
                ans+=1
                curr = points[i][1]
        return ans