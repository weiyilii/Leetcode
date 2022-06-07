# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        # check base
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        # outter: left.left, right.right
        # inner: left.right, right.left
        outter = self.helper(left.left, right.right)
        inner = self.helper(left.right, right.left)
        return outter and inner