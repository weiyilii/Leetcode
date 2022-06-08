# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 1st and 2nd keeps elements being swapped
        self.first, self.second = None, None
        # prev tracks current's previous node 
        self.prev = TreeNode(float('-inf'))
        
        def dfs(root):
            if root:
                dfs(root.left)
                if root.val < self.prev.val:
                    # first only need to be assigned for the first time
                    if not self.first:
                        self.first = self.prev
                    # second may change due to mistake places
                    self.second = root
                # prev also moves forward
                self.prev = root
                dfs(root.right)
            
        dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val