# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        d = set()
        
        def dfs(root):
            if not root:
                return False
            if k - root.val in d:
                return True
            d.add(root.val)
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)