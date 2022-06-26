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
        # Priority Queue
        from Queue import PriorityQueue
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        dummy = cur = ListNode()
        while not q.empty():
            min_node = q.get()[1]
            cur.next = min_node
            cur = cur.next
            min_node = min_node.next
            if min_node:
                q.put((min_node.val, min_node))
        return dummy.next