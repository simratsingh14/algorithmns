'''
Count the number of ways to word can be made using words in wordbank
Similar to Canconstruct
'''
memo = {}
def canConstruct(target,wordBank):
    if target in memo.keys():
        return memo[target]
    if target == '':
        return 1
    count = 0
    lar = list(filter(lambda x:target.startswith(x),wordBank))
    # print(lar,target)
    for i in lar:
        temp = canConstruct(target[len(i):],wordBank)
        count+=temp
    memo[target] = count
    return memo[target]

'''
Brute Force 
Time O(length(arr)^targetsize*targetsize)
Space O(targetsize^2)

Memoized Solution
Time O(length(arr)*targetsize*targetsize)
Space O(targetsize^2)

Tabulated Solution
Time O(length(arr)*targetsize*targetsize)
Space O(targetsize^2)
'''  

def countConstuctTabulation(target,wordBank):
    dp = [1] + [0]*len(target)
    for i in range(len(dp)):
        if dp[i] > 0:
            for j in range(len(wordBank)):
                if i+len(wordBank[j]) <= len(target) and wordBank[j].startswith(target[i]):
                    if target[:i] + wordBank[j] == target[:i+len(wordBank[j])]:
                        dp[i+len(wordBank[j])] += dp[i]
    # print(dp)
    return dp[len(target)]
                    



print(countConstuctTabulation('purple',['purp','p','ur','le','purpl']))
print(countConstuctTabulation('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(countConstuctTabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',['e'*1,'e'*2,'e'*3,'e'*4,'e'*5,'e'*6]))
