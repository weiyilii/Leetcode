/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy, p1 = list1, p2 = list2;
        ListNode temp = new ListNode(-1);
        while (p1 != null && p2 != null) {
            if (p1.val <= p2.val) {
                cur.next = p1;
                temp = p1.next;
                p1.next = null;
                p1 = temp;
            }
            else {
                cur.next = p2;
                temp = p2.next;
                p2.next = null;
                p2 = temp;  
            }
            cur = cur.next;
        }
        cur.next = (p1 == null ? p2 : p1);
        return dummy.next;
    }
}