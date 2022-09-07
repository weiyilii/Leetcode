# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = cur = ListNode(0)
        while list1 and list2:
            next1, next2 = list1.next, list2.next
            if list1.val <= list2.val:
                cur.next = list1
                list1.next = list2
                list1 = next1
            else:
                cur.next = list2
                list2.next = list1
                list2 = next2
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next