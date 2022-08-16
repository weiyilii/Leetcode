# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        q = deque([root])
        res = []
        while q:
            l = len(q)
            lsum = 0
            for _ in range(l):
                node = q.popleft()
                if node:
                    lsum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(float(lsum)/l)
        return res