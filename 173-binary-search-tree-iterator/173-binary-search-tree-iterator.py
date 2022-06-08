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
        self.stack = []
        self.push(root)
    # split inorder traversal using stack
    # everytime call next, pop and push left sub tree using dfs
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.push(node.right)
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False
        
    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left
            
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()