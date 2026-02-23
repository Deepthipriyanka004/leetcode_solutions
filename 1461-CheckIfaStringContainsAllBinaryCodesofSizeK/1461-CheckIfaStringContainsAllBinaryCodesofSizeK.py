# Last updated: 2/23/2026, 9:20:25 AM
1class Solution:
2  def hasAllCodes(self, s: str, k: int) -> bool:
3    n = 1 << k
4    if len(s) < n:
5      return False
6
7    # used[i] := True if i is a substring of `s`
8    used = [0] * n
9
10    windowStr = 0 if k == 1 else int(s[0:k - 1], 2)
11    for i in range(k - 1, len(s)):
12      # Include the s[i].
13      windowStr = (windowStr << 1) + int(s[i])
14      # Discard the s[i - k].
15      windowStr &= n - 1
16      used[windowStr] = True
17
18    return all(u for u in used)