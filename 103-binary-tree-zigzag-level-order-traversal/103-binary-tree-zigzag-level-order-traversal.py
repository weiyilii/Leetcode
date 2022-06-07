# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque()
        q.append(root)
        r = -1 # To control whether reverse sub list or not
        
        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if r == -1:
                    res.append(level)
                else:
                    res.append(level[::-1])
            r = r*(-1)
        return res