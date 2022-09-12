# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [1]
            left = dfs(root.left)
            right = dfs(root.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.res += 1
            return [n+1 for n in left + right if n+1 < distance]
        
        dfs(root)
        return self.res