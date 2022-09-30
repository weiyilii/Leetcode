# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        dummy = prev = ListNode(-1, head)
        for _ in range(n-1):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
            prev = prev.next
        prev.next = slow.next
        slow.next = None
        return dummy.next