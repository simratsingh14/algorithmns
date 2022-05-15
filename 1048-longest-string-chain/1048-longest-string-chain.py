class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x:len(x))
        def isChained(str1,str2):
            if len(str2) - len(str1) != 1:
                return False
            for i in range(len(str2)):
                if str1 ==  str2[:i] + str2[i+1:]:
                    return True
            return False
        dp = [1]*len(words)
        for i in range(1,len(words)):
            for j in range(len(words)):
                if isChained(words[j],words[i]):
                    dp[i] = max(dp[i],1+dp[j])
        
        #print(words,dp,isChained('xbc','cxbc'))
        return max(dp)
        
        