class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def word2pattern(word):
            representation = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            pattern = ''
            for i in word:
                pattern+=representation[ord(i)-ord('a')]
            return pattern
        s = set()
        for word in words:
            pattern = word2pattern(word)
            if pattern not in s:
                s.add(pattern)
        return len(s)
        
            
        