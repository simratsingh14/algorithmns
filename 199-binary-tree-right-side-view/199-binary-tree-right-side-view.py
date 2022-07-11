# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.d = {}
        def inorder(node,depth = 0):
            if node is None:
                return 
            
        
            self.d[depth] = node.val
            inorder(node.left,depth+1)
            inorder(node.right,depth+1)
            
        inorder(root)
        ans = []
        depth = 0
        #print(self.d)
        while depth in self.d:
            ans.append(self.d[depth])
            depth+=1
        return ans
        