# Last updated: 7/29/2026, 11:40:16 PM
1class Solution:
2  def __init__(self):
3    self.MAX = 10**6 + 1
4
5  def smallestPalindrome(self, s: str, k: int) -> str:
6    count = collections.Counter(s)
7    if not self._isPalindromePossible(count):
8      return ''
9
10    halfCount, midLetter = self._getHalfCountAndMidLetter(count)
11    totalPerm = self._calculateTotalPermutations(halfCount)
12    if k > totalPerm:
13      return ''
14    leftHalf = self._generateLeftHalf(halfCount, k)
15    return ''.join(leftHalf) + midLetter + ''.join(reversed(leftHalf))
16
17  def _isPalindromePossible(self, count: collections.Counter) -> bool:
18    oddCount = sum(1 for count in count.values() if count % 2 == 1)
19    return oddCount <= 1
20
21  def _getHalfCountAndMidLetter(self, count: collections.Counter) -> tuple[list[int], str]:
22    halfCount = [0] * 26
23    midLetter = ''
24    for c, freq in count.items():
25      halfCount[ord(c) - ord('a')] = freq // 2
26      if freq % 2 == 1:
27        midLetter = c
28    return halfCount, midLetter
29
30  def _calculateTotalPermutations(self, halfCount: list[int]) -> int:
31    """Calculate the total number of possible permutations."""
32    return self._countArrangements(halfCount)
33
34  def _generateLeftHalf(self, halfCount: list[int], k: int) -> list[str]:
35    """Generate the left half of the palindrome based on k."""
36    halfLen = sum(halfCount)
37    left = []
38    for _ in range(halfLen):
39      for i, freq in enumerate(halfCount):
40        if freq == 0:
41          continue
42        halfCount[i] -= 1
43        arrangements = self._countArrangements(halfCount)
44        if arrangements >= k:
45          left.append(chr(i + ord('a')))
46          break
47        else:
48          k -= arrangements
49          halfCount[i] += 1
50    return left
51
52  def _countArrangements(self, count: list[int]) -> int:
53    """Calculate the number of possible arrangements of characters."""
54    total = sum(count)
55    res = 1
56    for freq in count:
57      res *= self._nCk(total, freq)
58      if res >= self.MAX:
59        return self.MAX
60      total -= freq
61    return res
62
63  def _nCk(self, n: int, k: int) -> int:
64    res = 1
65    for i in range(1, min(k, n - k) + 1):
66      res = res * (n - i + 1) // i
67      if res >= self.MAX:
68        return self.MAX
69    return res