class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = defaultdict(lambda:6001)
        adj = defaultdict(list)
        for i in times:
            adj[i[0]].append((i[2],i[1]))   # distance,node
        distance[k] = 0
        pq = []
        heapq.heappush(pq,(0,k))
        while pq:
            elem = heapq.heappop(pq)
            weight = elem[0]
            node  = elem[1]
            if distance[node] < weight:
                continue 
            for i in adj[node]:
                w = i[0]
                v = i[1]
                if weight+w < distance[v]:
                    distance[v] = weight+w
                    heapq.heappush(pq,(weight+w,v))
        ans = max(distance.values())
        #print(distance)
        return -1 if len(distance) != n else ans
            
        