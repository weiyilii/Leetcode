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
        cur_a, cur_b = headA, headB
        m, n = 0, 0
        
        while cur_a:
            m += 1
            cur_a = cur_a.next
        while cur_b:
            n += 1
            cur_b = cur_b.next
        # After getting the length of both lists,
        # fast pointer should start iterating (m-n) steps so that they will meet at intersection
        if m <= n:
            slow, fast = headA, headB
        else:
            slow, fast = headB, headA
        
        for _ in range(abs(m-n)):
            fast = fast.next
            
        while fast and slow:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        
        return
