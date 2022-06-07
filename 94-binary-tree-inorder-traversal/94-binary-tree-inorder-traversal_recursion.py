# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
    # recursion
    def helper(self, root, res):
        if root == None:
            return
        # Left
        self.helper(root.left, res)
        # Root
        res.append(root.val)
        # Right
        self.helper(root.right, res)
