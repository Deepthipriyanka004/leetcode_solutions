// Last updated: 5/5/2026, 9:14:56 PM
1class Solution {
2  public ListNode rotateRight(ListNode head, int k) {
3    if (head == null || head.next == null || k == 0)
4      return head;
5
6    int length = 1;
7    ListNode tail = head;
8    for (; tail.next != null; tail = tail.next)
9      ++length;
10    tail.next = head; // Circle the list.
11
12    final int t = length - k % length;
13    for (int i = 0; i < t; ++i)
14      tail = tail.next;
15    ListNode newHead = tail.next;
16    tail.next = null;
17
18    return newHead;
19  }
20}