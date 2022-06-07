# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        cur = res = head
        new_end = ListNode(0, head)
        
        # new_start: 1st node in the sub linked list being reversed
        # new_end: the node before new_start
        for _ in range(left - 1):
            cur = cur.next
            new_end = new_end.next
        new_start = cur
        
        # reverse the sub linked list with a length of right - left + 1    
        prev = ListNode(0)
        for _ in range (right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # connect the old two pieces with the reversed part
        new_end.next = prev
        new_start.next = cur
        
        # if left == 1, head of result will be new_end next
        # or it will be res
        return (new_end.next if left == 1 else res)