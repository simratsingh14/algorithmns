import time
weight = [1, 3, 4, 5] 
val = [1, 4, 5, 7]
maximumWeight = 11
def knapsackUnboundedRecursive(n,maximumWeight):
    if maximumWeight == 0 or n == len(weight):
        return 0
    elif weight[n] > maximumWeight:
        return knapsackUnboundedRecursive(n+1,maximumWeight)
    else:
        return max(val[n]+knapsackUnboundedRecursive(n,maximumWeight-weight[n]),
                   knapsackUnboundedRecursive(n+1,maximumWeight))

start = time.time()
print(knapsackUnboundedRecursive(0,maximumWeight))
end = time.time()
print(f"time taken by recursive function {end-start}")  



def knapsackUnboundedTabulation(n,maximumWeight):
    dp = [[0]*(maximumWeight+1) for _ in range(n+1)]
    for length in range(1,len(dp)):
        for w in range(1,len(dp[0])):
            if weight[length-1] > w:
                dp[length][w] = dp[length-1][w]
            else:
                dp[length][w] = max(val[length-1]+dp[length][w-weight[length-1]],dp[length-1][w])
    # print(dp)
    return dp[n][maximumWeight]

start = time.time()
print(knapsackUnboundedTabulation(len(weight),maximumWeight))
end = time.time()
print(f"time taken by Tabulation function {end-start}")  