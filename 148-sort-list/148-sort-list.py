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
        if not head:
            return
        if not head.next:
            return head
        dummy = prev = ListNode(0, head)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwo(l1, l2)
    
    def mergeTwo(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwo(l1, l2.next)
            return l2