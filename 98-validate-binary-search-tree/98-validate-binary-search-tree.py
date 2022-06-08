# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -2**31-1, 2**31)
    
    def helper(self, root, l, r):
        if not root:
            return True
        if root.left and not (l < root.left.val and root.left.val < root.val):
            return False
        if root.right and not (root.val < root.right.val and root.right.val < r):
            return False
        return self.helper(root.left, l, root.val) and self.helper(root.right, root.val, r)