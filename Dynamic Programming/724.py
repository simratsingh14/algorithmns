# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].


class dp:
    def minCostStairRecursive(cost):  #This is giving TLE
        def minCostStair_helper(cost,total):
            if len(cost) <2:
                return total
            else:
                return(min(minCostStair_helper(cost[1:],total+cost[0]),minCostStair_helper(cost[2:],total+cost[1])))
        return minCostStair_helper(cost,0)

    def minCostStairDP(cost): # similarity with fibbonaci series
        numberofsteps = len(cost)
        dp = [None] * (len(cost)+1)
        dp[0] = 0 
        dp[1] = 0 
        dp[2] = min(dp[0]+cost[0],dp[1]+cost[1]) 
        
        for i in range(3,len(cost)+1):
            dp[i] =  min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        
        return dp[numberofsteps]

cost = [1,100,1,1,1,100,1,1,100,1]
print(dp.minCostStairDP(cost))

