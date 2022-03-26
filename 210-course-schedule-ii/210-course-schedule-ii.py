class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        indegree = [0]*numCourses
        for courses in prerequisites:
            d[courses[1]].append(courses[0])
            indegree[courses[0]]+=1
        q = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        ans = [i for i in range(len(indegree)) if indegree[i] == 0]
       # print(d,q,indegree)
        while q:
            elem = q.popleft()
            for val in d[elem]:
                indegree[val]-=1
                if indegree[val] == 0:
                    q.append(val)
                    ans.append(val)
    
        #print(ans)
        if len(ans) == numCourses:
            return ans
        return []
                    
        
        