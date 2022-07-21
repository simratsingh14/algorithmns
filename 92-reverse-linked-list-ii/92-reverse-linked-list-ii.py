# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        curr = ans = head 
        prev = None
        while left != count:
            nxt = curr.next
            
            prev = curr
            curr = nxt
            count += 1 
            
        saved = prev
        reverse = curr
        prev = None
        #print(saved,reverse)
        while curr is not None and count <= right:
            #print(curr.val)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count+=1
            
        if left == 1:
            ans = prev

            
        
        reverse.next = curr
        if saved is not None:
            saved.next = prev
        return ans
            
            
            
        