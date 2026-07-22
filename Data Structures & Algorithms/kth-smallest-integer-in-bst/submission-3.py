# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        curr = 0
        def dfs(node):
            nonlocal curr, res
            if not node or res is not None:
                return
            dfs(node.left)
            curr += 1
            if curr == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res