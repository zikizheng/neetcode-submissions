# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, minimum, maximum = stack.pop()

            if minimum < node.val < maximum:
                if node.left:
                    stack.append((node.left, minimum, node.val))
                if node.right:
                    stack.append((node.right, node.val, maximum))
            else:
                return False
        return True