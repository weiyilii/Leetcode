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
        :rtype: int
        """
        # DFS, Prefix Sum
        self.result = 0
        seen = collections.defaultdict(int)
        seen[0] = 1
        self.dfs(root, 0, seen, targetSum)
        return self.result
    
    def dfs(self, root, curSum, seen, targetSum):
        if root is None:
            return
        curSum += root.val
        if (curSum - targetSum) in seen:
            self.result += seen[curSum - targetSum]    
        seen[curSum] += 1
        self.dfs(root.left, curSum, seen, targetSum)
        self.dfs(root.right, curSum, seen, targetSum)
        # Important! After dfs on left and right child, it will move to another branch with a different parent node
        # curSum will be different, remove the previous one from seen
        seen[curSum] -= 1
