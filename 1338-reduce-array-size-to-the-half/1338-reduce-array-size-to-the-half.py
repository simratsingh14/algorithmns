class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = []
        c = Counter(arr)
        d = [(-j,i) for i,j in c.items()]
        #print(d)
        heapq.heapify(d)
        print(d)
        k = len(arr)
        ans = 0
        while k > len(arr)//2:
            num,_ = heapq.heappop(d)
            k+=num
            ans+=1
        return ans