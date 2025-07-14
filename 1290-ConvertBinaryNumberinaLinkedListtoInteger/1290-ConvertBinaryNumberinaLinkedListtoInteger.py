# Last updated: 7/14/2025, 10:56:56 AM
class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    ans = 0

    while head:
      ans = ans * 2 + head.val
      head = head.next

    return ans


