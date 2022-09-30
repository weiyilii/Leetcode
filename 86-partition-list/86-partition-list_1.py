# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = cur1 = ListNode(0)
        head2 = cur2 = ListNode(0)
        cur = head
        
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
                
            # For each cur node in the original list, after appending it to new sub list, dont forget to set its next to None, break original link
            temp = cur.next
            cur.next = None
            cur = temp
            
        cur1.next = head2.next
        
        return head1.next
        
