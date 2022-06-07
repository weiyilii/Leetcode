# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # base
        # if root is None, have gone through all levels, no p or q
        if not root:
            return None
        # if met p or q along the way (p != q), 
        # consider only the sub tree stretching from that root
        # that node (p or q) has been the highest ancestor of that sub tree
        # dont need to go deeper
        if p == root or q == root:
            return root
        # still not meeting p or q, having left and right temp nodes from sub trees
        leftnode = self.lowestCommonAncestor(root.left, p, q)
        rightnode = self.lowestCommonAncestor(root.right, p, q)
        # if leftnode is not none, then p is within left sub tree
        # if rightnode is not none, then q is within right sub tree
        # if p and q in each side, that root is LCA
        if leftnode and rightnode:
            return root
        # if one side is none, then p and q are both in left or right sub tree
        # return left child or right child
        if leftnode:
            return leftnode
        return rightnode