# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    min_diff = 10**5+1
    prev = -10**5-1
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.min_diff
    
    # Inorder traversal
    # prev records current root's previous value
    def dfs(self, root):
        if root:
            self.dfs(root.left) 
            diff = root.val - self.prev
            # if current diff less than min_diff
            # update min_diff
            if diff < self.min_diff:
                self.min_diff = diff
            # move prev forward as current root value
            self.prev = root.val
            self.dfs(root.right)
        return