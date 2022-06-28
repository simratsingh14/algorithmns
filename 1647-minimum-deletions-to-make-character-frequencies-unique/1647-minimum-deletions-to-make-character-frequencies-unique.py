class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        l = list(Counter(s).values())
        s = set()
        #print(l)
        for i in l:
            if i not in s:
                s.add(i)
            else:
                #print(i)
                count = i
                while count > 0 and count in s:
                    count-=1
                    ans+=1
                    #print(ans)
                if count!=0:
                    s.add(count)
        return ans