class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(src,graph,vis):
            vis[src] = 1
            for nbr in graph[src]:
                #print(nbr)
                if vis[nbr] == 0:
                    cycle = dfs(nbr,graph,vis)
                    #print(cycle)
                    if cycle:
                        return True
                elif vis[nbr] == 1:
                    return True
            vis[src] = 2
            return False
            
        
        vis = [0]*len(graph)
        ans = []
        for i in range(len(graph)):
            if vis[i]==0:
                cycle = dfs(i,graph,vis)
                if not cycle:
                    ans.append(i)
            elif vis[i] == 2:
                ans.append(i)
        #print(vis)
        return ans
            
        