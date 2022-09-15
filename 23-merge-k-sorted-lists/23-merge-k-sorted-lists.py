# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        left, right = 0, len(lists) - 1
        mid = left + (right - left)//2
        lefthalf = self.mergeKLists(lists[:mid+1])
        righthalf = self.mergeKLists(lists[mid+1:])
        return self.mergeTwo(lefthalf, righthalf)
    
    def mergeTwo(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwo(l1, l2.next)
            return l2