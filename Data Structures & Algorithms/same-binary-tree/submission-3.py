# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l, r = [p], [q]
        while l and r:
            nodeP = l.pop()
            nodeQ = r.pop()
            if not nodeP and not nodeQ:
                continue
            elif not nodeP or not nodeQ:
                return False
            if (nodeP.val != nodeQ.val):
                return False
            l.append(nodeP.left)
            r.append(nodeQ.left)
            l.append(nodeP.right)
            r.append(nodeQ.right)
        return True
        