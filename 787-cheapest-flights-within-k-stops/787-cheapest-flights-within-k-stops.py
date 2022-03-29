class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [10e4+1]*n
        curr = [10e4+1]*n
        prev[src] = 0
        curr[src] = 0
        for i in range(k+1):
            unchanged = True
            for flight in flights:
                s = flight[0]
                d = flight[1]
                cost = flight[2]
                if prev[s] + cost < curr[d]:
                    curr[d] = prev[s] + cost
                    unchanged = False
            prev[:] = curr
            if unchanged:
                break
        return curr[dst] if curr[dst] != 10e4+1 else -1
                    
                