# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res, path = [], []
        self.dfs(root, targetSum, path, res)
        return res
        
    def dfs(self, root, targetSum, path, res):
        if not root:
            return
        if not root.left and not root.right:
            # only when root has no child and root.val matches targetSum
            # this path satisfies, append it to res
            if root.val == targetSum:
                return res.append(path+[root.val])
            return
        self.dfs(root.left, targetSum-root.val, path+[root.val], res)
        self.dfs(root.right, targetSum-root.val, path+[root.val], res)
        return