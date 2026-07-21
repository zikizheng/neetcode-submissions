# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialise(self, node):
        if not node:
            return "@#"
        return ("#" + str(node.val) + self.serialise(node.left) + self.serialise(node.right))

    def zFunction(self, s: String):
        n = len(s)
        z = [0] * n
        l, r = 0, 0

        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while z[i] + i < n and s[z[i]] == s[z[i] + i]:
                z[i] += 1
            if z[i] + i > r:
                l, r = i, z[i] + i
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sRoot = self.serialise(root)
        sSubRoot = self.serialise(subRoot)

        combine = sSubRoot + "$" + sRoot

        z = self.zFunction(combine)

        for i in range(len(sSubRoot) + 1, len(combine)):
            if z[i] == len(sSubRoot):
                return True
        return False