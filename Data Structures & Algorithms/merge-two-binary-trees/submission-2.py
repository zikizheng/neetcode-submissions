# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        curr = root = TreeNode()
        q = collections.deque([[curr, root1, root2]])
        while q:
            curr, node1, node2 = q.popleft()
            if node1 and node2:
                curr.val = node1.val + node2.val
            elif node1:
                curr.val = node1.val
            elif node2:
                curr.val = node2.val
            if (node1 and node1.left) or (node2 and node2.left):
                curr.left = TreeNode()
                q.append((curr.left, node1.left if node1 else None, node2.left if node2 else None))
            if (node1 and node1.right) or (node2 and node2.right):
                curr.right = TreeNode()
                q.append((curr.right, node1.right if node1 else None, node2.right if node2 else None))
        return root