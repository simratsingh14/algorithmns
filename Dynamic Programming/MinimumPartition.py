"""
Sum of subset differences
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example:
Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 

"""

arr = [1,5,6,11]

def subsetsumTabulation(n,target):
    dp = [[True]+[False]*(target) for _ in range(n+1)]
    for arrSize in range(1,len(dp)):
        for targetSum in range(1,len(dp[0])):
            if arr[arrSize-1] > targetSum:
                dp[arrSize][targetSum] = dp[arrSize-1][targetSum]
            else:
                dp[arrSize][targetSum] = dp[arrSize-1][targetSum] or dp[arrSize-1][targetSum -arr[arrSize-1]]
    # print(dp)
    return dp[-1]

def minimumPartionDifference(n,arr = arr):
    t =  subsetsumTabulation(n,sum(arr))
    for i in range(sum(arr)//2,-1,-1):
        if t[i]:
            return sum(arr) - 2*i
    

print(minimumPartionDifference(len(arr)))
