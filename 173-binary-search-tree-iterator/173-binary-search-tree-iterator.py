# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.traversal(self.root, self.stack)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop(0).val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False
        
    def traversal(self, root, stack):
        if root:
            self.traversal(root.left, stack)
            stack.append(root)
            self.traversal(root.right, stack)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()