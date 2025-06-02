// Last updated: 6/2/2025, 6:31:31 PM
class Solution {
 public:
  ListNode* insertGreatestCommonDivisors(ListNode* head) {
    for (ListNode* curr = head; curr->next != nullptr;) {
      ListNode* inserted =
          new ListNode(__gcd(curr->val, curr->next->val), curr->next);
      curr->next = inserted;
      curr = inserted->next;
    }
    return head;
  }
};