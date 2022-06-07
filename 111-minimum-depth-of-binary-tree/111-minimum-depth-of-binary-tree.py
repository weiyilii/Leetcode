# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # root is None: return 0
        # root is leaf (no left or right child): return 1
        # root has only one child: find minDepth given that child as root then + 1
        # root has 2 children: min of 2 minDepth based on left and right node then + 1
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        if not root.left or not root.right:
            return self.minDepth(root.left) + 1 if root.left else self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1