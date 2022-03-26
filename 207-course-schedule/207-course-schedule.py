class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        indegree = [0]*numCourses
        for i in prerequisites:
            d[i[1]].append(i[0])
            indegree[i[0]]+=1
        #print(d,indegree)
        
        q = collections.deque()
        done = set()
        for inx,val in enumerate(indegree):
            if not val:
                q.append(inx)
                done.add(inx)
        #print(q)
        
        while q:
            #print(q,indegree)
            elem = q.popleft()
            for i in d[elem]:
                indegree[i]-=1
                if indegree[i] == 0:
                    done.add(i)
                    q.append(i)
        return len(done) == numCourses
                    