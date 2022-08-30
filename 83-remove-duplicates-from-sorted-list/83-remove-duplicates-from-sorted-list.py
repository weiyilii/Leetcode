# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(-101, head)
        cur = head
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next