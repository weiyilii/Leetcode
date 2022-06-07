# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # Given a root, find depth of left and right sub trees and compare
        left_height = self.helper(root.left)
        right_height = self.helper(root.right)
        # if not balanced, return False
        if abs(left_height - right_height) > 1:
            return False
        # if balanced at this root, move forward to compare having both children as root
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # helper function gives max depth given any root
    def helper(self, root):
        if not root:
            return 0
        return max(self.helper(root.left), self.helper(root.right)) + 1