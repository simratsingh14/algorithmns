# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for _ in range(m)]
        si,sj,ei,ej = 0,0,m-1,n-1
        node = head
        while node is not None:
            i = sj
            while node is not None and i <= ej:
                mat[si][i] = node.val
                node = node.next
                i+=1
            si+=1
            
            i = si
            while node is not None and i <= ei:
                mat[i][ej] = node.val
                node = node.next
                i+=1
            ej-=1
            i = ej
            while node is not None and i >= sj:
                mat[ei][i] = node.val
                node = node.next
                i-=1
            ei-=1
            i = ei
            while node is not None and i >= si:
                mat[i][sj] = node.val
                node = node.next
                i-=1
            sj+=1
        return mat
                
                
                
                
                
                
                