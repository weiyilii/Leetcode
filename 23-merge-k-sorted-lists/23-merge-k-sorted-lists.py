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
        # Compare one by one
        min_index = 0
        dummy = cur = ListNode()
        # if_break controls if all nodes have been visited
        if_break = False
        
        while not if_break:
            min_val = 10**4+1
            if_break = True
            for i in range(len(lists)):
                if lists[i]:
                    if_break = False
                    node = lists[i]
                    if node.val < min_val:
                        min_index, min_val = i, node.val
            if not if_break:
                cur.next = lists[min_index]
                lists[min_index] = lists[min_index].next
                cur = cur.next
        return dummy.next