"""
There is only one character 'A' on the screen of a notepad. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
"""

n = 51
def minSteps(n):
    dp = [-1,0] + [0]*(n-1)
    for i in range(2,n+1):
        if biggestDivisor(i) == 1:
            dp[i] = i
        else:
            dp[i] = dp[biggestDivisor(i)] + i//(biggestDivisor(i))  
    print(dp)
    return dp[n]

def biggestDivisor(n):
    for i in range(n//2,0,-1):
        if n % i == 0:
            return i

# print(biggestDivisor(51))

# print(minSteps(n))
def minStepsRecursive(n):
    if n == 1:
        return 0
    if biggestDivisor(n) == 1:
        return n
    else:
        return minStepsRecursive(biggestDivisor(n)) + n//biggestDivisor(n)

print(minStepsRecursive(n))
    


    
    