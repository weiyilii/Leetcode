# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.height = float('-inf')
        def findHeight(root, level):
            if not root:
                return
            self.height = max(level, self.height)
            findHeight(root.left, level + 1)
            findHeight(root.right, level + 1)
        findHeight(root, 0)
        
        m, n = self.height+1, 2**(self.height+1)-1
        matrix = [["" for j in range(n)] for i in range(m)]
        
        def dfs(root, i, j):
            if not root:
                return
            matrix[i][j] = str(root.val)
            dfs(root.left, i+1, j-2**(self.height-i-1))
            dfs(root.right, i+1, j+2**(self.height-i-1))
        dfs(root, 0, (n-1)//2)
        return matrix
            