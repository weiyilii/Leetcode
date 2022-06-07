# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0, head)
        pairs = {}
        
        while head:
            pairs[head] = None
            head = head.next
            prev = prev.next
            
            if prev.next in pairs:
                return prev.next
        
        return
