# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            # if root less than p, q, lca must be within left sub tree
            if root.val > p.val and root.val > q.val:
                root = root.left
            # if root greater than p, q, lca must be within right sub tree
            elif root.val < p.val and root.val < q.val:
                root = root.right
            # if p and q are in each side (or equal to root), lca is current root
            else:
                return root