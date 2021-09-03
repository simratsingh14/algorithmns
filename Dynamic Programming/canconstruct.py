'''
It takes a target word and we have to tell whether we can construct it or not using array known as wordbank
'''


def canConstruct(target,wordBank):
    memo = {}                        # Added for memoization
    def helper_function(target):
        if len(target) == 0:
            return True
        lar = list(filter(lambda x:target.startswith(x),wordBank))
        # print(lar,target)
        if len(lar) == 0:
            return False
        
        for i in lar:
            if i in memo.keys():
                ans = memo[i]          # Added for memoization   
            else:
                ans = helper_function(target[len(i):])
                memo[i] = ans          # Added for memoization

            if ans:
                return ans
        return False
    return helper_function(target)

'''
Brute Force 
Time O(length(arr)^targetsize*targetsize)
Space O(targetsize^2)

Memoized Solution
Time O(length(arr)*targetsize*targetsize)
Space O(targetsize^2)
'''

target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesf'
wordBank = ['e'*1,'e'*2,'e'*3,'e'*4,'e'*5,'e'*6]
print(canConstruct(target,wordBank))



