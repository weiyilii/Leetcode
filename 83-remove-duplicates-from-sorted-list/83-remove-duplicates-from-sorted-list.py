# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-200, head)
        prev, cur = dummy, head
        while cur:
            if cur.val == prev.val:
                temp = cur.next
                prev.next = temp
                cur.next = None
                cur = temp
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next