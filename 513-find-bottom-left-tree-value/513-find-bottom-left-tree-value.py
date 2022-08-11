# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            res = []
            for _ in range(l):
                node = q.popleft()
                if node:
                    res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return res[0]