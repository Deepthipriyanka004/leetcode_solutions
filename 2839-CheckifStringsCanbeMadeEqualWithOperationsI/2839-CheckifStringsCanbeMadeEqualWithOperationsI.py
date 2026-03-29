# Last updated: 3/29/2026, 9:50:53 AM
1class Solution:
2  def canBeEqual(self, s1: str, s2: str) -> bool:
3    def swappedStrings(s: str) -> list[str]:
4      chars = list(s)
5      return [chars,
6              ''.join([chars[2], chars[1], chars[0], chars[3]]),
7              ''.join([chars[0], chars[3], chars[2], chars[1]]),
8              ''.join([chars[2], chars[3], chars[0], chars[1]])]
9
10    return any(a == b
11               for a in swappedStrings(s1)
12               for b in swappedStrings(s2))