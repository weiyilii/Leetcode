# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return 
        elif len(lists) == 1:
            return lists[0]
        else:
            left, right = 0, len(lists) - 1
            mid = left + (right - left) // 2
            l1 = self.mergeKLists(lists[left:mid + 1])
            l2 = self.mergeKLists(lists[mid + 1:right + 1])
            return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2