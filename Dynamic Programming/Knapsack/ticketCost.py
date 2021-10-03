from functools import lru_cache
'''
You have planned some train traveling one year in advance. 
The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365
'''

days = [1,3,4,5,6,7,12]
costs = [2,7,15]


def minCostTicket(days,costs):
    dp = {}
    @lru_cache(None)
    
    def minCostTicketRescursive(passTillday,n):
        if (passTillday,n) in dp.keys():
            return dp[(passTillday,n)]
        if n == len(days):
                return 0
        if days[n] <= passTillday:
            dp[(passTillday,n)] = minCostTicketRescursive(passTillday,n+1)
            return dp[(passTillday,n)]
        else:
            dp[(passTillday,n)] = min(costs[0] + minCostTicketRescursive(days[n],n+1),
                       costs[1] + minCostTicketRescursive(days[n]+6,n+1),
                       costs[2] + minCostTicketRescursive(days[n]+29,n+1))
            return dp[(passTillday,n)]
    return minCostTicketRescursive(0,0)
   
print(minCostTicket(days,costs))     



