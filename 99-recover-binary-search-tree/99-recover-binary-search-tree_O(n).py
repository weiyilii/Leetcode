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
        # store all nodes walked through inorder traversal
        nodes = []
        self.helper(root, nodes)
        # from start to end find 1st node which next val is less than current node val
        i = 0
        while nodes[i].val < nodes[i+1].val:
            i += 1
        first = nodes[i]
        # from end to start find 2nd node which previous val is greater than current node val
        j = len(nodes) - 1
        while nodes[j].val > nodes[j-1].val:
            j -= 1
        second = nodes[j]
        # 1st and 2nd are the mistake ones, swap their values
        first.val, second.val = second.val, first.val
        return root
    
    # Inorder traversal    
    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            res.append(node)
            self.helper(node.right, res)
        return
