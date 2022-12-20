class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = set([0])
        q = deque()
        q.append(0)
        while q:
            curr = q.popleft()
            #print(curr,self.visited)
            for room in rooms[curr]:
                if room not in self.visited:
                    q.append(room)
                    self.visited.add(room)
        return len(self.visited) == len(rooms)
        
        
        