class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for inx,word in enumerate(s):
            hashmap[word] = inx
        print(hashmap)
        maxv = 0
        prev = -1
        res = []
        for inx,word in enumerate(s):
            maxv = max(maxv,hashmap[word])
            if maxv == inx:
                res.append(maxv-prev)
                prev = maxv
        return res
            
        