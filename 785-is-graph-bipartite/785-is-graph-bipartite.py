class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def isEven(graph,src,visited):
            color = 0
            q = [src]
            while q:
                size = len(q)
                for _ in range(size):
                    elem = q.pop(0)
                    if visited[elem] != -1:
                        if visited[elem]!= color:
                            return False
                        else:
                            continue
                    visited[elem] = color
                    for i in graph[elem]:
                        if visited[i] == -1:
                            q.append(i)
                color = ~color
            return True
        visited = [-1]*len(graph)
        for i in range(len(graph)):
            if visited[i] == -1:
                if not isEven(graph,i,visited):
                    return False
        return True
                
