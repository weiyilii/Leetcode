# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def dfs(node):
            if not node:
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if not left or not right:
                return False
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False
            self.res += 1
            return True
        
        dfs(root)
        return self.res
            
        