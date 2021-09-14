"""
A weight array and value array is given maximize the profit given a maximum weight list
"""

def knapsackRecursive(weight,val,maximumWeight):
    if len(weight) == 0 or maximumWeight == 0:
        return 0
    else:
        w = weight.pop()
        v = val.pop()
        if maximumWeight < w:
            return knapsackRecursive(weight,val,maximumWeight)
        else:
            print(v,w,val,weight,maximumWeight)
            return max(v+knapsackRecursive(weight,val,maximumWeight-w),knapsackRecursive(weight,val,maximumWeight))

val = [60, 100, 120]
wt = [10, 20, 30]
maximumWeight = 50

print(knapsackRecursive(wt,val,maximumWeight))