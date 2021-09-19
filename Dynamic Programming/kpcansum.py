'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
'''

arr = [3, 34, 4, 12, 5, 2]
target = 30
def subsetsumRecursive(n,target):
    if n == len(arr) and target!=0 :
        return False
    if target == 0:
        return True
    elif arr[n] > target:
        return subsetsumRecursive(n+1,target)
    else:
        return subsetsumRecursive(n+1,target-arr[n]) or subsetsumRecursive(n+1,target)

print(subsetsumRecursive(0,target))
    

def subsetsumTabulation(n,target):
    dp = [[True]+[False]*(target) for _ in range(n+1)]
    for arrSize in range(1,len(dp)):
        for targetSum in range(1,len(dp[0])):
            if arr[arrSize-1] > targetSum:
                dp[arrSize][targetSum] = dp[arrSize-1][targetSum]
            else:
                dp[arrSize][targetSum] = dp[arrSize-1][targetSum] or dp[arrSize-1][targetSum -arr[arrSize-1]]
    # print(dp)
    return dp[-1][-1] 
                  
print(subsetsumTabulation(len(arr),target))