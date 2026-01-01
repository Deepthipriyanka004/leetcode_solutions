# Last updated: 1/1/2026, 8:58:39 AM
1class Solution:
2  def plusOne(self, digits: list[int]) -> list[int]:
3    for i, d in reversed(list(enumerate(digits))):
4      if d < 9:
5        digits[i] += 1
6        return digits
7      digits[i] = 0
8
9    return [1] + digits