# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        l, last = 1, head
        
        while last.next:
            l += 1
            last = last.next        
        k = k%l
        
        # First connect both ends like a circle
        last.next = head
        
        # Find the right place to break the circle
        # Then new head is the right node
        # Left node should be linked to None
        temp = head
        for _ in range(l - k - 1):
            temp = temp.next
        new_head = temp.next
        temp.next = None
        
        return new_head
        