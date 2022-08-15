class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.arr = []
        
        def recursive(start,end,temp=[]):
            #print(start,end,temp,s[start:end],s[start:end][::-1])
            if end == len(s):
                if s[start:end] == s[start:end][::-1]:
                    temp.append(s[start:end])
                    self.arr.append(temp)
                    return 
                else:
                    return 
            if s[start:end] == s[start:end:][::-1]:
                recursive(end,end+1,temp+[s[start:end]])
            recursive(start,end+1,temp)
        recursive(0,1)
        return self.arr
        
                
                
                
        