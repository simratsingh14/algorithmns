# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        node = head 
        ans = head
        node2 = head
        num = k - 1
        while num:
            node = node.next
            node2 = node2.next
            num-=1
        node3 = head
        node2 = node2.next
        while node2:
            node2 = node2.next 
            node3 = node3.next
       # print(node3.val,node.val)
        node3.val,node.val = node.val,node3.val
        return ans
        
        
        