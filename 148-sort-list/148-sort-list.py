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
        # Divide and Conquer, Merge Sort, Iterative
        if not head or not head.next:
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
        dummy = cur = ListNode(0)
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
