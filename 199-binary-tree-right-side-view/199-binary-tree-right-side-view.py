# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS
        res = []
        q = collections.deque()
        q.append(root)
        # Use queue: FIFO
        # Append from right to left
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    # If i == 0, node is the right most in current level
                    if i == 0:
                        res.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
        return res