

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
	    
	    h = [[nums[i],i] for i in range(len(nums))]
	    h.sort(key= lambda x:x[0])
	    #print(h)
	    count = 0
	    for i in range(len(h)):
	        _,j = h[i]
	        swap = 1
	        while j!=i:
	            swap+=1
	            newIndex = h[j][1]
	            h[j][1] = j  # now it is correct
	            j = newIndex
	        count+=swap-1
	        #print(h)
	    return count
	            
	            
	            
	            
	            
		#Code here


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends