'''
Find the minimum possible length of sum to a target value
'''
def bestSum(target,array):
    dp = [None]*(target+1)
    dp[0] = []
    for i in range(len(dp)):
        if dp[i] is not None:
            for j in range(len(array)):
                if i + array[j] < len(dp):
                    if dp[i+array[j]] is None:
                        dp[i+array[j]] = dp[i] + [array[j]]
                    else:
                        dp[i+array[j]] = dp[i] + [array[j]] if len(dp[i] + [array[j]]) < len(dp[i+array[j]]) else dp[i+array[j]]
                        
    # print(dp)
    return dp[-1]

target = 100
array = [25,1,5,2]
print(bestSum(target,array))
                        
'''
Time Complexity is O(nm2)
Time Complexity is O(m2)

'''