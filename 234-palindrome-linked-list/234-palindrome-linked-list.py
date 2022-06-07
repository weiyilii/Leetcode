# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        prev, slow, fast = None, head, head
        # Use slow to find mid point while reversing the first half
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        # if fast, then list has odd. slow needs to skip the center
        if fast:
            slow = slow.next
        # now prev leads the first reversed half; slow leads the second
        while prev:
            if slow.val != prev.val:
                return False
            slow, prev = slow.next, prev.next
        return True