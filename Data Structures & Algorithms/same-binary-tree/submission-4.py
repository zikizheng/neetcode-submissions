# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s = [(p, q)]
        while s:
            i, j = s.pop()
            if not i and not j:
                continue
            elif not i or not j or i.val != j.val:
                return False
            s.append((i.left, j.left))
            s.append((i.right, j.right))
        return True