class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #print(set(words[0]).intersection(set(words[1])))
        ans = 0
        for i in range(len(words)):
            for j in range(i,len(words)):
                inter = set(words[i]).intersection(set(words[j]))
                if len(inter) == 0:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
                
        