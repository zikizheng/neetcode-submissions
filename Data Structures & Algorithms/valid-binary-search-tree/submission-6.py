# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([(root, float("-inf"), float("inf"))])
        
        while q:
            node, l, r = q.popleft()
            if not node:
                continue
            elif l < node.val < r:
                q.append((node.left, l, node.val))
                q.append((node.right, node.val, r))
            else:
                return False
        return True