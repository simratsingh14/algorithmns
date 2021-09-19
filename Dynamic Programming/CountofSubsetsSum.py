"""
Count of subsets sum with a Given sum
Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.
Example:

Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}

"""

arr = [1, 2, 3, 4, 5]
target = 10

def CountSubsetSumTabulation(n,target):
    dp = [[1] + [0]*(target) for j in range(n+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    # print(dp)
    return dp[-1][-1]
print(CountSubsetSumTabulation(len(arr),target)) 
