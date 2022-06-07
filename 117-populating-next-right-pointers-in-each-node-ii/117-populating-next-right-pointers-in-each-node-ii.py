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
        cur = root
        prev = head = None
        while cur:
            if cur.left:
                if prev:
                    prev.next = cur.left
                prev = cur.left
                if not head:
                    head = prev
            if cur.right:
                if prev:
                    prev.next = cur.right
                prev = cur.right
                if not head:
                    head = prev
            cur = cur.next
            if not cur:
                cur = head
                prev = head = None
        return root
                
        