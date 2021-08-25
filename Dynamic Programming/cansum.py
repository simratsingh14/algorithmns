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


k = canSummemo([7,14],300)
print(k)
        
                



            




