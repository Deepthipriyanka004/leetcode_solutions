# Last updated: 3/31/2026, 12:47:48 PM
1class Solution:
2  def generateString(self, str1: str, str2: str) -> str:
3    n = len(str1)
4    m = len(str2)
5    sz = n + m - 1
6    ans = [None] * sz
7    modifiable = [True] * sz
8
9    # 1. Handle all 'T' positions first.
10    for i, tf in enumerate(str1):
11      if tf == 'T':
12        for j, c in enumerate(str2):
13          pos = i + j
14          if ans[pos] and ans[pos] != c:
15            return ''
16          ans[pos] = c
17          modifiable[pos] = False
18
19    # 2. Fill all remaining positions with 'a'.
20    for i in range(sz):
21      if not ans[i]:
22        ans[i] = 'a'
23
24    # 3. Handle all 'F' positions.
25    for i in range(n):
26      if str1[i] == 'F' and self._match(ans, i, str2):
27        modifiablePos = self._lastModifiablePosition(i, m, modifiable)
28        if modifiablePos == -1:
29          return ''
30        ans[modifiablePos] = 'b'
31        modifiable[modifiablePos] = False
32
33    return ''.join(ans)
34
35  def _match(self, ans: list, i: int, s: str) -> bool:
36    """Returns True if the substring of ans starting at `i` matches `s`."""
37    for j, c in enumerate(s):
38      if ans[i + j] != c:
39        return False
40    return True
41
42  def _lastModifiablePosition(self, i: int, m: int, modifiable: list) -> int:
43    """
44    Finds the last modifiable position in the substring of ans starting at `i`.
45    """
46    modifiablePos = -1
47    for j in range(m):
48      pos = i + j
49      if modifiable[pos]:
50        modifiablePos = pos
51    return modifiablePos