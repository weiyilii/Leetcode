# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    prev = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root
    
    # Reversed inorder traversal: right -> root -> left
    # nodes will be visited descendingly
    def dfs(self, root):
        if root:
            self.dfs(root.right)
            # prev = accumalted sum of visited nodes 
            self.prev += root.val
            root.val = self.prev
            self.dfs(root.left)
        return