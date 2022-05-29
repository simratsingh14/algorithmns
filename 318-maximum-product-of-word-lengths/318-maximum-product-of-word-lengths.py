class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #print(set(words[0]).intersection(set(words[1])))
        ans = 0
        d = defaultdict(int)
        for word in words:
            for l in word:
                d[word] |= 1 << (ord(l)-ord('a'))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if d[words[i]] & d[words[j]] == 0:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
        