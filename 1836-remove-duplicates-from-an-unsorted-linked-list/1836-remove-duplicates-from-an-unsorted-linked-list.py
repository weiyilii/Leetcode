# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = {}
        cur = head
        while cur:
            if cur.val in count:
                count[cur.val] += 1
            else:
                count[cur.val] = 1
            cur = cur.next
        
        dummy = prev = ListNode(0, head)
        cur = head
        while cur:
            if count[cur.val] > 1:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next