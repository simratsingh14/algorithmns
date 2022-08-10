class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr = 0
        x,y = 0,0
        dr = [(1,0),(0,1),(-1,0),(0,-1)]          # 0,1,2,3
        for i in 4*instructions:
            if i == 'L':
                curr-=1
            elif i == 'R':
                curr+=1
            curr%=4
            if i == 'G':
                x+=dr[curr][0]
                y+=dr[curr][1]
        return x == 0 and y == 0 
                
                
        