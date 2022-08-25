class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = Counter(magazine)
        r = Counter(ransomNote)
        #print(s,r)
        for i in r.keys():
            if r[i] > s[i]:
                return False
        return True
        