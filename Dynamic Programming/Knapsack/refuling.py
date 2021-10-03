"""
Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
"""
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

def refuelingPetrol(target,startFuel,stations):
    n = len(stations)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(len(dp)):
        dp[i][0] = startFuel
    for i in range(1,len(dp)):
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j]

            if dp[i-1][j-1] >= stations[i-1][0]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+stations[i-1][1])
    
    print(dp)
    for i in range(n+1):
        if dp[n][i] >= target:
            return i
    return -1


print(refuelingPetrol(target,startFuel,stations))
