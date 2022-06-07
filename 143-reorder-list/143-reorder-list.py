# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # step 1: mid point find mid point (slow) then break
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # second half list starts from new_start
        new_head = slow.next
        # break list from slow (mid point)
        slow.next = None

        # step 2: reverse second half
        prev, cur = None, new_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        new_head = prev

        # step 3: combine 2 parts starting from head and new_head
        head1, head2 = head, new_head
        while head2:
            next1 = head1.next
            next2 = head2.next
            
            head1.next = head2
            head1 = next1
            
            head2.next = next1
            head2 = next2
        
        
        