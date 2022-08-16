"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                for child in cur.children:
                    stack.append(child)
        return res[::-1]