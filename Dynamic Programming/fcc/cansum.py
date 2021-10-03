# Problem in https://www.youtube.com/watch?v=oBt53YbR9Kk&t=4282s
# find if sum is possible using element of array

# Recursive Solution
# Input numbers:-   list
       #targetSum:- Int

def canSum(numbers,targetSum):

    def canSum_helper(targetSum):
        val = False
        if targetSum == 0:
            # print(targetSum)
            return True
        elif targetSum < min(numbers):
            return False
        else:
            lar = [x for x in numbers if x <= targetSum]
            print(lar,targetSum)
            for i in lar:
                val = canSum_helper(targetSum-i)
                if val:
                    # print(i)
                    return True
        return False
    return canSum_helper(targetSum)

# Memoize Solution
# Input numbers:-   list
       #targetSum:- Int

def canSummemo(numbers,targetSum):
    memo = {}
    def canSum_helper(targetSum):
        val = False
        if targetSum == 0:
            # print(targetSum)
            return True
        elif targetSum < min(numbers):
            return False
        else:
            if targetSum in memo.keys():
                return memo[targetSum]
            lar = [x for x in numbers if x <= targetSum]
            print(lar,targetSum)
            for i in lar:
                memo[targetSum-i] = canSum_helper(targetSum-i)
                if memo[targetSum-i]:
                    # print(i)
                    memo[targetSum]=True
                    return True
        memo[targetSum] = False            
        return memo[targetSum]
    return canSum_helper(targetSum)


# k = canSummemo([7,14],300)
# print(k)
        
# Tabulation Methold
'''
Time complexity is O(nm)
Space complexity is O(m)
'''

def canSum_tabulation(numbers,target):
    dp = [False]*(target+1)
    dp[0] = True
    for i in range(len(dp)):
        if dp[i]:
            for j in range(len(numbers)):
                if i + numbers[j] < len(dp):
                    dp[i+numbers[j]] = True
    return dp[-1]


print(canSum_tabulation([2,3,5],8))



