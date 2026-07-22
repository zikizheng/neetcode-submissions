# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = collections.deque([(p, q)])
        while q:
            i, j = q.popleft()
            if not i and not j:
                continue
            elif not i or not j or i.val != j.val:
                return False
            q.append((i.left, j.left))
            q.append((i.right, j.right))
        return True