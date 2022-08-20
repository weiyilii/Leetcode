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
        self.res = False
        
        def dfs(root):
            if not root:
                return
            if k - root.val in d:
                self.res = True
                return
            d.add(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.res