# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.d = defaultdict(list)
        def helper(root,val):
            if root is None:
                return 
            helper(root.left,val+1)
            self.d[val].append(root.val)
            helper(root.right,val+1)
        helper(root,val = 0)
        #print(self.d,max(self.d))
        return sum(self.d[max(self.d)])
        
            
            
        