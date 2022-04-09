class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(-1*time,num) for num,time in Counter(nums).items()]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            x,y = heapq.heappop(heap)
            ans.append(y)
        return ans
        