# Last updated: 8/16/2025, 6:03:34 PM
class Solution:
  def maximum69Number(self, num: int) -> int:
    return int(str(num).replace('6', '9', 1))