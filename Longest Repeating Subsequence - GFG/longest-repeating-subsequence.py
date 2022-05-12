#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		prev = [0]*(len(str)+1)
		curr = [0]*(len(str)+1)
		for i in range(1,len(prev)):
		    for j in range(1,len(curr)):
		        if i==j:
		            continue
		        elif str[i-1] == str[j-1]:
		            curr[j] = 1 + prev[j-1]
		        else:
		            curr[j] = max(prev[j],curr[j-1])
		    prev = curr[:]
	    return prev[-1]
		            
		           

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends