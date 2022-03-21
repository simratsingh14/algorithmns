class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]*len(rooms)
        def dfs(node,rooms):
            visited[node] = 1
            
            for i in rooms[node]:
                if not visited[i]:
                    dfs(i,rooms)
            
        dfs(0,rooms)
        return all(visited)
        