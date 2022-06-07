# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        # Concating 2 lists and 2 pointers will meet 
        # when iterating through another list
        # a + b = b + a
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a