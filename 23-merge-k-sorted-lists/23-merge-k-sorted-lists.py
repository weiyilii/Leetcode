# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 0:
            return None
        if l == 1:
            return lists[0]
        left, right = 0, l - 1
        mid = left + (right - left) // 2
        lefthalf = self.mergeKLists(lists[left:mid + 1])
        righthalf = self.mergeKLists(lists[mid+1:right+1])
        return self.mergeTwo(lefthalf, righthalf)
    
    def mergeTwo(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = cur = ListNode(0)
        while l1 and l2:
            x, y = l1.val, l2.val
            if x <= y:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next