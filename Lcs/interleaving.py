"""
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

"""
s1 = "a"
s2 = "b"
s3 = "a"
from functools import cache
def isInterleave(s1,s2,s3) -> bool:
    @cache
    def isInterleaveRecursive(s1_inx,s2_inx,s3_inx):
        # print(s1_inx,s2_inx,s3_inx)
        if s1_inx == len(s1) and s2_inx == len(s2) and s3_inx == len(s3):
            return True
        elif s1_inx < len(s1) and s2_inx < len(s2) and s3_inx < len(s3):
            if s1[s1_inx] == s3[s3_inx] and s2[s2_inx] == s3[s3_inx]:
                return isInterleaveRecursive(s1_inx+1,s2_inx,s3_inx+1) or isInterleaveRecursive(s1_inx,s2_inx+1,s3_inx+1)
            elif s1[s1_inx] == s3[s3_inx]:
                return isInterleaveRecursive(s1_inx+1,s2_inx,s3_inx+1)
            elif s2[s2_inx] == s3[s3_inx]:
                return isInterleaveRecursive(s1_inx,s2_inx+1,s3_inx+1)
        elif s1_inx < len(s1) and s3_inx < len(s3):
            if s1[s1_inx] == s3[s3_inx]:
                return isInterleaveRecursive(s1_inx+1,s2_inx,s3_inx+1)
        elif s2_inx < len(s2) and s3_inx < len(s3):
            if s2[s2_inx] == s3[s3_inx]:
                return isInterleaveRecursive(s1_inx,s2_inx+1,s3_inx+1)
        return False

    return isInterleaveRecursive(0,0,0)


print(isInterleave(s1,s2,s3))
        
        


        