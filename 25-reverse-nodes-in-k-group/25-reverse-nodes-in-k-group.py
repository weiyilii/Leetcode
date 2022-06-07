# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        
        while cur:
            count += 1
            cur = cur.next
        
        if count < k or k <= 1:
            return head     
        else:
            cur,res = head, head
            prev = ListNode(0)
            prev.next = head
            i = 0
            while i < k:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                i += 1
            head = prev
            new_start = cur
            res.next = self.reverseKGroup(new_start, k)
            return head
            