# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ssf =0 
        def helper(root):
            if root is None:
                return None
            root.right = helper(root.right)
            self.ssf += root.val
            root.val = self.ssf
            root.left = helper(root.left)
            return root
        return helper(root)
        