# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if (abs(target - node.val) < abs(target - res)):
                    res = node.val
                elif (abs(target - node.val) == abs(target - res)):
                    res = min(node.val, res)
                stack.append(node.left)
                stack.append(node.right)
        return res