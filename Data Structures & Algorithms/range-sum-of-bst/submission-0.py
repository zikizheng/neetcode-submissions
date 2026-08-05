# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return sum(res)