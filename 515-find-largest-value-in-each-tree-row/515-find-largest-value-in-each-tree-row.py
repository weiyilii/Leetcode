# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            row_max = float('-inf')
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                if node:
                    row_max = max(row_max, node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(row_max)
        return res