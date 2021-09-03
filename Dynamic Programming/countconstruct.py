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
'''  

target = 'enterapotentpot'
wordBank = ['a','p','ent','enter','ot','o','t']
print(canConstruct(target,wordBank))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',['e'*1,'e'*2,'e'*3,'e'*4,'e'*5,'e'*6]))
