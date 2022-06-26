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
        # Heap as Priority Queue
        from heapq import *
        h = []
        for l in lists:
            if l:
                heappush(h, (l.val, l))
        dummy = cur = ListNode()
        while h:
            min_node = heappop(h)[1]
            cur.next = min_node
            cur = cur.next
            min_node = min_node.next
            if min_node:
                heappush(h, (min_node.val, min_node))
        return dummy.next
