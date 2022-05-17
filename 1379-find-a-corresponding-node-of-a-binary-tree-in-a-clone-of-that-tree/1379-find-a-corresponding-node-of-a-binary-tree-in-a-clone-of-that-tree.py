# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def inorder(root):
            if root is None:
                return None
            val1 = inorder(root.left)
            if root.val == target.val:
                return root
            val2 = inorder(root.right)
            if val1 is None:
                return val2
            if val2 is None:
                return val1
            
        return inorder(cloned)
        