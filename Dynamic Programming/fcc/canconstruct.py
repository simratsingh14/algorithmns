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
                ans = memo[i]          # Added from memoization   
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

Tabulation Solution
Time O(length(arr)*targetsize*targetsize)
Space O(targetsize^2)
'''


def canConstructTab(target,wordBank):
    dp = [False]*(len(target)+1)
    dp[0] = True
    for i in range(len(dp)):
        if dp[i]:
            for j in range(len(wordBank)):
                if i+len(wordBank[j]) <= len(target) and wordBank[j].startswith(target[i]):
                    if target[:i] + wordBank[j] == target[:i+len(wordBank[j])]:
                        dp[i+len(wordBank[j])] = True
                        
    print(dp)
    return dp[-1]



target = 'enterapotentpot'
wordBank = ['a','p','ent','enter','ot','o','t']
print(canConstructTab(target,wordBank))



