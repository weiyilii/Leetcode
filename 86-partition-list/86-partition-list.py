# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = ListNode(0)
        right = ListNode(0)
        cur_left, cur_right = left, right
        
        while head:
            if head.val < x:
                cur_left.next = head
                cur_left = cur_left.next               
            else:
                cur_right.next = head
                cur_right = cur_right.next 
            head = head.next
        
        cur_right.next = None
        
        cur_left.next = right.next
        
        return left.next