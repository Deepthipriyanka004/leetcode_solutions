# Last updated: 12/24/2025, 1:19:50 PM
1class Solution:
2  def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
3    appleSum = sum(apple)
4    capacitySum = 0
5
6    for i, c in enumerate(sorted(capacity, reverse=True)):
7      capacitySum += c
8      if capacitySum >= appleSum:
9        return i + 1
10
11    return len(capacity)