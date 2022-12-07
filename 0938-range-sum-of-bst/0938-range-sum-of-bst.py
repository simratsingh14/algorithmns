# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.ans = 0
        def inorder(node):
            if node is None:
                return 
            if low <= node.val <= high:
                self.ans+=node.val
            inorder(node.left)
            inorder(node.right)
        inorder(root)
        return self.ans
        