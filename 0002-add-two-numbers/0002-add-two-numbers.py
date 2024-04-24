# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = head = ListNode(0, None)
        extra = 0
        while l1 or l2 or extra != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            s = val1 + val2 + extra
            cur.next = ListNode(s%10, None)
            extra = s//10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            cur = cur.next
        return head.next
        