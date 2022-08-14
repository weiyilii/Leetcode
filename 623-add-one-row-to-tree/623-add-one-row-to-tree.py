# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        from collections import deque
        
        if depth == 1:
            new = TreeNode(val, left = root)
            return new
        
        q = deque([root])
        level = 1
        while level < depth - 1:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            level += 1
        while q:
            node = q.popleft()
            newleft = TreeNode(val, left = node.left)
            newright = TreeNode(val, right = node.right)
            node.left = newleft
            node.right = newright
        return root
            