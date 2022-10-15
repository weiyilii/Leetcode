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
    public ListNode partition(ListNode head, int x) {
        ListNode p1 = new ListNode(-1), p2 = new ListNode(-1);
        ListNode dummy1 = p1, dummy2 = p2;
        ListNode temp = new ListNode(-1);
        while (head != null) {
            if (head.val < x) {
                p1.next = head;
                p1 = p1.next;
            }
            else {
                p2.next = head;
                p2 = p2.next;
            }
            temp = head.next;
            head.next = null;
            head = temp;
        }
        p1.next = dummy2.next;
        return dummy1.next;
    }
}