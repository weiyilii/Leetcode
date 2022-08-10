"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(head):
            nonlocal pre
            if head is None:
                return None
            if pre is not None:
                pre.next = head
                head.prev = pre
            pre = head
            nxt = head.next
            head.next = None
            child = head.child
            head.child = None
            dfs(child)
            dfs(nxt)
            
        pre = None
        dfs(head)
        return head