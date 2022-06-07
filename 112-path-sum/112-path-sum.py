# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # if root is None return false
        if root is None:
            return False
        # if root has no child, check targetSum and root.val
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
            return False
        # root may has 1 or 2 children, check both sub trees with updated targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)