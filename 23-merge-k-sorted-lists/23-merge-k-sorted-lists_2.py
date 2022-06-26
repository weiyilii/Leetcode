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
        def merge2lists(l1, l2):
            dummy = cur = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            return dummy.next
        # Divide and conquer
        # l[0] = merge(l[0], l[1]), l[2] = merge(l[2], l[3]), l[4] = merge(l[4], l[5]) ....
        # l[0] = merge(l[0], l[2]), l[4] = merge(l[4], l[6]), ....
        # l[0] = merge(l[0], l[4])
        # return l[0]
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount-interval, interval*2):
                lists[i] = merge2lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else None
