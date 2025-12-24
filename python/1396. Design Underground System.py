from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.average_time_info = defaultdict(lambda: defaultdict(lambda: (0,0)))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.customers[id]
        end_station, end_time = stationName, t
        summation, cnt = self.average_time_info[start_station][end_station]
        self.average_time_info[start_station][end_station] = (summation+end_time-start_time, cnt+1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        summation, cnt = self.average_time_info[startStation][endStation]
        return summation / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)