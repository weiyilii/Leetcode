# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd, even = head, head.next
        # keep the head of even sub list
        even_head = even
        while even and even.next:
            # skip odd.next which is even; same for even.next
            odd.next = odd.next.next
            even.next = even.next.next
            # update current odd and even node
            odd = odd.next
            even = even.next
        # now odd points to the end of odd sub list;
        # link it to to even_head
        odd.next = even_head
        return head