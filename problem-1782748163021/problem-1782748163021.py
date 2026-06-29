# Last updated: 6/29/2026, 9:19:23 PM
1class Solution:
2  def numOfStrings(self, patterns: list[str], word: str) -> int:
3    return sum(pattern in word for pattern in patterns)