# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def counsturct(preorder,inorder,preStart,preEnd,inStart,inEnd):
            if preStart > preEnd:
                return None
            if preStart == preEnd:
                return TreeNode(preorder[preEnd])
            rootVal = preorder[preStart]
            root = TreeNode(rootVal)
            #print(preStart,preEnd,inStart,inEnd)
            inx = inorder.index(rootVal,inStart,inEnd+1)   # index at which rootValue is Found
            count = inx - inStart
            root.left = counsturct(preorder,inorder,preStart+1,preStart+count,inStart,inStart+inx-1)
            root.right = counsturct(preorder,inorder,preStart+count+1,preEnd,inx+1,inEnd)
            return root
        return counsturct(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)
        
        