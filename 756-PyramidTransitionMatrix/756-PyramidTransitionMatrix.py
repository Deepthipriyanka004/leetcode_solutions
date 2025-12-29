# Last updated: 12/29/2025, 6:34:18 PM
1class Solution:
2  def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
3    prefixToBlocks = collections.defaultdict(list)
4
5    for a in allowed:
6      prefixToBlocks[a[:2]].append(a[2])
7
8    def dfs(row: str, nextRow: str, i: int) -> bool:
9      if len(row) == 1:
10        return True
11      if len(nextRow) + 1 == len(row):
12        return dfs(nextRow, '', 0)
13
14      for c in prefixToBlocks[row[i:i + 2]]:
15        if dfs(row, nextRow + c, i + 1):
16          return True
17
18      return False
19
20    return dfs(bottom, '', 0)