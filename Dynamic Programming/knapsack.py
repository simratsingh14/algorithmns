import functools
import time
"""
A weight array and value array is given maximize the profit given a maximum weight list
"""

weight = [10, 20, 30]
val = [60, 100, 120]
maximumWeight = 50

# @functools.cache
def knapsackRecursive(n,maximumWeight):
    if len(weight) == n or maximumWeight == 0:
        return 0
    else:
        w = weight[n]
        v = val[n]
        if maximumWeight < w:
            return knapsackRecursive(n+1,maximumWeight)
        else:
            return max(knapsackRecursive(n+1,maximumWeight),v+knapsackRecursive(n+1,maximumWeight-w))


start = time.time()  
print(knapsackRecursive(0,maximumWeight))
end = time.time()
print(f"time taken by recursive function {end-start}")  


