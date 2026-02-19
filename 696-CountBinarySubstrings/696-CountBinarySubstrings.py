# Last updated: 2/19/2026, 9:25:26 PM
1class Solution:
2  def countBinarySubstrings(self, s: str) -> int:
3    ans = 0
4    prevCount = 0
5    equals = 1
6
7    for i in range(len(s) - 1):
8      if s[i] == s[i + 1]:
9        equals += 1
10      else:
11        ans += min(prevCount, equals)
12        prevCount = equals
13        equals = 1
14
15    return ans + min(prevCount, equals)