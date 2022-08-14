# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        # Revursive DFS
        if depth == 1:
            new = TreeNode(val, left = root)
            return new
        
        def dfs(node, level):
            if not node:
                return
            if level == depth - 1:
                newleft = TreeNode(val, left = node.left)
                newright = TreeNode(val, right = node.right)
                node.left, node.right = newleft, newright
                return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 1)
        return root
            
