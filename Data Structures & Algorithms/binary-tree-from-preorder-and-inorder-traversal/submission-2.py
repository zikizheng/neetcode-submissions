# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val: i for i, val in enumerate(inorder)}

        pre = 0

        def dfs(l, r):
            nonlocal pre
            
            if l > r:
                return None
            
            v = preorder[pre]
            pre += 1
            m = index[v]

            return TreeNode(v,
                            dfs(l, m - 1),
                            dfs(m + 1, r))

        return dfs(0, len(inorder) - 1)