# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.dfs(root)
        return max(res)
    
    def dfs(self, root):
        if root is None:
            return [0, 0]
        res = [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res