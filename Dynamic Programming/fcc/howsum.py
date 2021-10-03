def howsum(target,arr):
    ans = []
    final = [] 
    def helper(target,ans):
        if target == 0:
            final.append(ans)
            return ans
        elif target < min(arr):
            return
        else:
            # lar = [x for x in arr if x <= target]
            lar = list(filter(lambda x:x<=target,arr))
            print(lar,target,ans)
            for i in sorted(lar,reverse=True):
                helper(target-i,ans+[i])
            
                    
    helper(target,[])
    if len(final):
        return final
    else:
        return -1
target = 32
arr = [1,2,4]
# print(howsum(target,arr))
def howSumTabulation(target,arr):
    dp = [None]*(target+1)
    dp[0] = []
    for i in range(len(dp)):
        if isinstance(dp[i],list):
            for j in range(len(arr)):
                if arr[j] + i < len(dp):
                    dp[arr[j] + i] = dp[i] + [arr[j]]
    # print(dp)
    return dp[-1]

print(howSumTabulation(target,arr))
'''
Tabulation Methold
Time Complexity O(m2n)
Space Complexity O(m2)
'''