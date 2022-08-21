# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        q = deque([(1, root)])
        res = 1
        while q:
            l = len(q)
            res = max(res, q[-1][0] - q[0][0] + 1)
            for _ in range(l):
                n, node = q.popleft()
                if node:
                    if node.left:
                        q.append((2*n, node.left))
                    if node.right:
                        q.append((2*n+1, node.right))
        return res