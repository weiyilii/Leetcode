"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        l, r, n = root.left, root.right, root.next
        if l:
            l.next = r
            if n:
                r.next = n.left
            self.connect(l)
            self.connect(r)
        return root
