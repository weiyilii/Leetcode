# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.seen = collections.defaultdict(list)
        self.dfs(root, 0)
        max_level = max(self.seen.keys())
        return self.seen[max_level][0]
    
    def dfs(self, root, level):
        if root is None:
            return
        self.seen[level].append(root.val)
        level += 1
        self.dfs(root.left, level)
        self.dfs(root.right, level)