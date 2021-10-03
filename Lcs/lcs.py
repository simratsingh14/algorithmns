"""
Longest Common Subsequence Problem solution using Memoization
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

For example, “abc”,  “abg”, “bdf”, “aeg”,  ‘”acefg”, .. etc are subsequences of “abcdefg”.

"""

str1 = "ABC"
str2 = "AB"


def lcs(str1,str2):
    if str1 == '' or str2 == '':
        return 0
    else:
        if str2[-1] == str1[-1]:
            return 1 + lcs(str1[:-1],str2[:-1])
        else:
            return max(lcs(str1,str2[:-1]),lcs(str1[:-1],str2))

print(lcs(str1,str2))

