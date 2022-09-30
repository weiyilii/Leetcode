# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-200, head)
        cur = head
        val = -200
        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    prev.next = cur.next
                    temp = cur.next
                    cur.next = None
                    cur = temp
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next