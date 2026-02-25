# Last updated: 2/25/2026, 9:16:58 PM
1class Solution:
2  def sortByBits(self, arr: list[int]) -> list[int]:
3    return sorted(arr, key=lambda x: (x.bit_count(), x))