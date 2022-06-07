# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        # First element of preorder is always root
        val = preorder.pop(0)
        # Find the index of root from inorder
        # Left sub array of inorder is left sub tree
        # Right gives right sub tree
        ind = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(preorder, inorder[:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root
        