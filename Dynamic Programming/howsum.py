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
target = 8
arr = [2,3,5]
print(howsum(target,arr))
