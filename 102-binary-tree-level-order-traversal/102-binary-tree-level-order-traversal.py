# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque() # FIFO: first in first out
        q.append(root)
        
        while q:
            # now q only has elements of current level
            # qlen makes sure we go through only current level
            qlen = len(q)
            level = []
            for _ in range(qlen):
                # popleft every element in the current level
                node = q.popleft()
                # if node is not null, append its left and right child to q
                # append node.val to level storeing values of current level
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # only append level(sub list) to result when not empty
            if level:
                res.append(level)
        
        return res