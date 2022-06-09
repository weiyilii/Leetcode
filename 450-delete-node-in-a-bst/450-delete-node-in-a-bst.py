# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        # if root.val < key, key node is in right sub tree
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        # key node is in left sub tree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # current root is key, delete root
        else:
            # if root only has right child, just return right
            if not root.left:
                return root.right
            # root only has left child, return left
            elif not root.right:
                return root.left
            # root have both left and right sub tree
            # travers right sub tree and find its minimum node
            # copy minimum value to root (root is what we want to delete)
            # and delete node with minimum value
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                # set root.right to the deleted root pointer!
                root.right = self.deleteNode(root.right, cur.val)
        return root