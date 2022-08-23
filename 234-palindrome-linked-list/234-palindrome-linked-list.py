# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lar = []
        node = head
        while node is not None:
            lar.append(node.val)
            node = node.next
        return lar == lar[::-1]
        