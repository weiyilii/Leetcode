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
        def remove(cur):
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            return            
            
        res = cur = head
        
        while cur:
            remove(cur)
            cur = cur.next
        
        return res