class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i-j].append(mat[i][j])
        d1 = {}
        for k in d.keys():
            d1[k] = 0
            d[k].sort()
        #print(d1,d)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                inx = d1[i-j]
                mat[i][j] = d[i-j][inx]
                d1[i-j]+=1
        return mat
                
        