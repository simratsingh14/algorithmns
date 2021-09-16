
weight = [1, 3, 4, 5]  
val = [10, 40, 50, 70]
maximumWeight = 8
def knapsackUnboundedRecursive(n,maximumWeight):
    if maximumWeight == 0 or n == len(weight):
        return 0
    elif weight[n] > maximumWeight:
        return knapsackUnboundedRecursive(n+1,maximumWeight)
    else:
        return max(val[n]+knapsackUnboundedRecursive(n,maximumWeight-weight[n]),
                   knapsackUnboundedRecursive(n+1,maximumWeight))

print(knapsackUnboundedRecursive(0,maximumWeight))