# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        elif not root.left and not root.right:
            return str(root.val)
        elif not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        else:
            return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"