# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p == root or q == root:
            return root
        leftnode = self.lowestCommonAncestor(root.left, p, q)
        rightnode = self.lowestCommonAncestor(root.right, p, q)
        if leftnode and rightnode:
            return root
        return leftnode if leftnode else rightnode