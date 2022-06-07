#Function: Reverse a linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):  
    def reverseLinkedList(self, head):  
        """  
        :type head: ListNode. 
        :type k: int.  
        :rtype: ListNode
        """  
        prev, cur = None, head
        while cur:   
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev
        return head
