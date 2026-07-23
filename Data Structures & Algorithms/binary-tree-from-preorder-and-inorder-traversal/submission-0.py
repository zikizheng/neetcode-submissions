# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        for m in range(len(inorder)):
            if inorder[m] == preorder[0]:
                break
        
        return TreeNode(val = preorder[0], 
                left = self.buildTree(preorder[1: m + 1], inorder[0: m]), 
                right = self.buildTree(preorder[m + 1:], inorder[m + 1:]))