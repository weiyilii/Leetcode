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
        def reverseLinkedlist(head):
            prev = None
            cur = head
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            head = prev
            return head
        
        l1 = reverseLinkedlist(l1)
        l2 = reverseLinkedlist(l2)
        
        carrier = 0
        dummy = cur = ListNode()
        
        while l1 or l2 or carrier:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            carrier, num = divmod(x+y+carrier, 10)
            cur.next= ListNode(num)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        res = reverseLinkedlist(dummy.next)
        return res
        