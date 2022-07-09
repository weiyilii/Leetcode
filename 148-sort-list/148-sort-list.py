# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def getMid(self, head):
        prev = ListNode(0, head)
        mid = head
        while head and head.next:
            mid = mid.next
            prev = prev.next
            head = head.next.next
        prev.next = None
        return mid
    
    def merge(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            x, y = l1.val, l2.val
            if x <= y:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next