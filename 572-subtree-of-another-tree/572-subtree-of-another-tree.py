# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        if self.dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def dfs(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)