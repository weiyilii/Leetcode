# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n), Space: O(n)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Dictionary records all nodes we went through
        # key: head, value: next
        pairs = {}
        prev = ListNode(0, head)
        
        while head:
            pairs[head] = head.next
            head = head.next
            prev = prev.next
            if prev.next in pairs:
                return True
        
        return False
