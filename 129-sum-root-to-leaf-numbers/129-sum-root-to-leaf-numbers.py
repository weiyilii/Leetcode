# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # path records every node val as string along DFS
        path = ""
        # everytime reaches leaf, append int(path) to res
        res = []
        self.dfs(root, path, res)
        return sum(res)
        
    def dfs(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(int(path+str(root.val)))
            return
        self.dfs(root.left, path+str(root.val), res)
        self.dfs(root.right, path+str(root.val), res)
        return