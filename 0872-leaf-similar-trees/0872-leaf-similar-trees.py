# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.arr1 = []
        self.arr2 = []
        
        def inorder(node,arr):
            if node is None:
                return
            if node.left is None and node.right is None:
                arr.append(node.val)
            inorder(node.left,arr)
            inorder(node.right,arr)
        inorder(root1,self.arr1)
        inorder(root2,self.arr2)
        #print(self.arr1,self.arr2)
        return self.arr1 == self.arr2
            
        