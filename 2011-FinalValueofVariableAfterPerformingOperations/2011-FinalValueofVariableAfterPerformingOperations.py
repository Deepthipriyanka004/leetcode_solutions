# Last updated: 10/20/2025, 2:36:00 PM
class Solution:
  def finalValueAfterOperations(self, operations: list[str]) -> int:
    return sum(op[1] == '+' or -1 for op in operations)