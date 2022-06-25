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
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        carrier, dummy = 0, None
        while s1 or s2 or carrier:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0
            carrier, num = divmod(x+y+carrier, 10)
            new = ListNode(num)
            new.next = dummy
            dummy = new
        return dummy
