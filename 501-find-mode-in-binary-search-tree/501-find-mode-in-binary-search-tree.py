# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = []
    count = 0
    max_count = 0
    prev = TreeNode(0)
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.res
    
    # Basic mechanism: Inorder traversal
    # Use prev to record current root's previous node and compare their values
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            
            # count frequency of each value
            if root.val == self.prev.val:
                self.count += 1
            else:
                self.count = 1
            # compare count with max_count
            # if > max_count, current value is mode
            # update max_count and res
            if self.count > self.max_count:
                self.res = [root.val]
                self.max_count = self.count
            # if equal, append current value to res
            elif self.count == self.max_count:
                self.res.append(root.val)
            # update prev to current root and move on
            self.prev = root
            
            self.dfs(root.right)
        return
        