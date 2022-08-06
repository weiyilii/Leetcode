# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        
        def dfs(root): 
            nonlocal max_path
            if root is None:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            cur_path = left + right + root.val
            max_path = max(cur_path, max_path)
            return root.val + max(left, right)
        
        dfs(root)
        return max_path