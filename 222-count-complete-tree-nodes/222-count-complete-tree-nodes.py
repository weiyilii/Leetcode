# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ld, rd = self.getDepth(root.left), self.getDepth(root.right)
        # if left and right depth same, then right sub tree might not be perfect
        # if left - right = 1, right must be perfect, count left sub
        if ld == rd:
            return 2**(ld) + self.countNodes(root.right)
        return self.countNodes(root.left) + 2**rd
    
    # helper function gets depth given root
    def getDepth(self, root):
        if not root:
            return 0
        # move to root.left because complete binary tree is as far left as possible
        return self.getDepth(root.left) + 1