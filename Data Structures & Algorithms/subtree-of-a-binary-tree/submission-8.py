# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s_root = self.serialise(root)
        s_subRoot = self.serialise(subRoot)

        s = s_subRoot + "$" + s_root

        z = self.zAlg(s)

        for i in z:
            if i == len(s_subRoot):
                return True
        return False

    def serialise(self, node):
        if not node:
            return "#"
        return ("@" + str(node.val) + self.serialise(node.left) + self.serialise(node.right))
    
    def zAlg(self, s):
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