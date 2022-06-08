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
        nodes = []
        self.helper(root, nodes)
        i = 0
        while nodes[i].val < nodes[i+1].val:
            i += 1
        first = nodes[i]
        j = len(nodes) - 1
        while nodes[j].val > nodes[j-1].val:
            j -= 1
        second = nodes[j]
        first.val, second.val = second.val, first.val
        return root
        
    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            res.append(node)
            self.helper(node.right, res)
        return