# Last updated: 7/22/2026, 11:39:16 PM
1from dataclasses import dataclass
2
3
4@dataclass
5class Group:
6  start: int
7  length: int
8
9
10class SparseTable:
11  def __init__(self, nums: list[int]):
12    self.n = len(nums)
13    # st[i][j] := max(nums[j..j + 2^i - 1])
14    self.st = [[0] * (self.n + 1) for _ in range(self.n.bit_length() + 1)]
15    self.st[0] = nums.copy()
16    for i in range(1, self.n.bit_length() + 1):
17      for j in range(self.n - (1 << i) + 1):
18        self.st[i][j] = max(
19            self.st[i - 1][j],
20            self.st[i - 1][j + (1 << (i - 1))])
21
22  def query(self, l: int, r: int) -> int:
23    """Returns max(nums[l..r])."""
24    i = (r - l + 1).bit_length() - 1
25    return max(self.st[i][l], self.st[i][r - (1 << i) + 1])
26
27
28class Solution:
29  def maxActiveSectionsAfterTrade(
30      self,
31      s: str,
32      queries: list[list[int]]
33  ) -> list[int]:
34    ones = s.count('1')
35    zeroGroups, zeroGroupIndex = self._getZeroGroups(s)
36    if not zeroGroups:
37      return [ones] * len(queries)
38
39    st = SparseTable(self._getZeroMergeLengths(zeroGroups))
40
41    def getMaxActiveSections(l: int, r: int) -> int:
42      left = (-1 if zeroGroupIndex[l] == -1
43              else (zeroGroups[zeroGroupIndex[l]].length -
44                    (l - zeroGroups[zeroGroupIndex[l]].start)))
45      right = (-1 if zeroGroupIndex[r] == -1
46               else (r - zeroGroups[zeroGroupIndex[r]].start + 1))
47      startAdjacentGroupIndex, endAdjacentGroupIndex = self._mapToAdjacentGroupIndices(
48          zeroGroupIndex[l] + 1, zeroGroupIndex[r] if s[r] == '1' else zeroGroupIndex[r] - 1)
49      activeSections = ones
50      if (s[l] == '0' and s[r] == '0' and
51              zeroGroupIndex[l] + 1 == zeroGroupIndex[r]):
52        activeSections = max(activeSections, ones + left + right)
53      elif startAdjacentGroupIndex <= endAdjacentGroupIndex:
54        activeSections = max(
55            activeSections,
56            ones + st.query(startAdjacentGroupIndex, endAdjacentGroupIndex))
57      if (s[l] == '0' and
58          zeroGroupIndex[l] + 1 <= (zeroGroupIndex[r]
59                                    if s[r] == '1' else zeroGroupIndex[r] - 1)):
60        activeSections = max(activeSections, ones + left +
61                             zeroGroups[zeroGroupIndex[l] + 1].length)
62      if (s[r] == '0' and zeroGroupIndex[l] < zeroGroupIndex[r] - 1):
63        activeSections = max(activeSections, ones + right +
64                             zeroGroups[zeroGroupIndex[r] - 1].length)
65      return activeSections
66
67    return [getMaxActiveSections(l, r) for l, r in queries]
68
69  def _getZeroGroups(self, s: str) -> tuple[list[Group], list[int]]:
70    """
71    Returns the zero groups and the index of the zero group that contains the
72    i-th character.
73    """
74    zeroGroups = []
75    zeroGroupIndex = []
76    for i in range(len(s)):
77      if s[i] == '0':
78        if i > 0 and s[i - 1] == '0':
79          zeroGroups[-1].length += 1
80        else:
81          zeroGroups.append(Group(i, 1))
82      zeroGroupIndex.append(len(zeroGroups) - 1)
83    return zeroGroups, zeroGroupIndex
84
85  def _getZeroMergeLengths(self, zeroGroups: list[Group]) -> list[int]:
86    """Returns the sums of the lengths of the adjacent groups."""
87    return [a.length + b.length for a, b in itertools.pairwise(zeroGroups)]
88
89  def _mapToAdjacentGroupIndices(
90      self,
91      startGroupIndex: int,
92      endGroupIndex: int
93  ) -> tuple[int, int]:
94    """
95    Returns the indices of the adjacent groups that contain l and r completely.
96
97    e.g.    groupIndices = [0, 1, 2, 3]
98    adjacentGroupIndices = [0 (0, 1), 1 (1, 2), 2 (2, 3)]
99    map(startGroupIndex = 1, endGroupIndex = 3) -> (1, 2)
100    """
101    return startGroupIndex, endGroupIndex - 1