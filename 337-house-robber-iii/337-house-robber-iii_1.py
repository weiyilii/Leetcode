# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # DFS, DP
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp = dict()
        res = self.dfs(root, dp)
        return res
    
    def dfs(self, root, dp):
        if root is None:
            return 0
        if root in dp:
            return dp[root]
        
        val = 0
        if root.left:
            val += self.dfs(root.left.left, dp) + self.dfs(root.left.right, dp)
        if root.right:
            val += self.dfs(root.right.left, dp) + self.dfs(root.right.right, dp)
            
        dp[root] = max(root.val+val, self.dfs(root.left, dp)+self.dfs(root.right, dp))
        return dp[root]
