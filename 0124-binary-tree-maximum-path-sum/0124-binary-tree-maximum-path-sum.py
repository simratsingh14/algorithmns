# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1000
        def dfs(root):
            if root is None:
                return 0
            lpath = max(0,dfs(root.left))
            rpath = max(0,dfs(root.right))
            self.ans = max(self.ans,lpath+rpath+root.val)
            return max(lpath,rpath) + root.val
        dfs(root)
        return self.ans