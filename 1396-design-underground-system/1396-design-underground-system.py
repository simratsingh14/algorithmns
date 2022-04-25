class UndergroundSystem:

    def __init__(self):
        self.times = defaultdict(int)
        self.checkin = {}
        self.averagetime = defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startd,starttime = self.checkin[id]
        self.times[(startd,stationName)] += 1
        times = self.times[(startd,stationName)]
        self.averagetime[(startd,stationName)] = (self.averagetime[(startd,stationName)]*(times-1) + (t-starttime))/times
        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averagetime[(startStation,endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)