class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def isInterleaveRecursive(s1_inx,s2_inx,s3_inx):
        # print(s1_inx,s2_inx,s3_inx)
            if s1_inx == len(s1) and s2_inx == len(s2) and s3_inx == len(s3):
                return True
            elif s1_inx < len(s1) and s2_inx < len(s2) and s3_inx < len(s3):
                if s1[s1_inx] == s3[s3_inx] and s2[s2_inx] == s3[s3_inx]:
                    return isInterleaveRecursive(s1_inx+1,s2_inx,s3_inx+1) or isInterleaveRecursive(s1_inx,s2_inx+1,s3_inx+1)
                elif s1[s1_inx] == s3[s3_inx] and s3_inx < len(s3):
                    return isInterleaveRecursive(s1_inx+1,s2_inx,s3_inx+1)
                elif s2[s2_inx] == s3[s3_inx] and s3_inx < len(s3):
                    return isInterleaveRecursive(s1_inx,s2_inx+1,s3_inx+1)
            elif s1_inx < len(s1) and s3_inx < len(s3):
                if s1[s1_inx] == s3[s3_inx]:
                    return isInterleaveRecursive(s1_inx+1,s2_inx,s3_inx+1)
            elif s2_inx < len(s2) and s3_inx < len(s3):
                if s2[s2_inx] == s3[s3_inx]:
                    return isInterleaveRecursive(s1_inx,s2_inx+1,s3_inx+1)
            return False

        return isInterleaveRecursive(0,0,0)
