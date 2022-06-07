# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l1 = l2 = head
        res = l2
        
        for _ in range(n):
            l1 = l1.next
        
        if not l1:
            return res.next
        
        while l1.next:
            l1 = l1.next
            l2 = l2.next
        
        l2.next = l2.next.next
        
        return res