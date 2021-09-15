import functools
import time
"""
A weight array and value array is given maximize the profit given a maximum weight list
"""

weight = [1,3,4,5]
val = [1,4,5,7]
maximumWeight = 7

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


dar = {}
def knapsackRecursiveMemoization(n,maximumWeight):
    if (n,maximumWeight) in dar.keys():
        return dar[(n,maximumWeight)] 
    if len(weight) == n or maximumWeight == 0:
        return 0
    else:
        w = weight[n]
        v = val[n]
        if maximumWeight < w:
            dar[(n,maximumWeight)] = knapsackRecursive(n+1,maximumWeight) 
            return dar[(n,maximumWeight)] 
        else:
            dar[(n,maximumWeight)] = max(knapsackRecursive(n+1,maximumWeight),v+knapsackRecursive(n+1,maximumWeight-w)) 
            return dar[(n,maximumWeight)] 


start = time.time()  
print(knapsackRecursiveMemoization(0,maximumWeight))
end = time.time()
print(f"time taken by recursive+memoization function {end-start}")  

