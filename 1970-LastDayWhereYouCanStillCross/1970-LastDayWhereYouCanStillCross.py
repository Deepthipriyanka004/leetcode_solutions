# Last updated: 12/31/2025, 11:36:02 AM
1class Solution:
2  def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
3    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
4
5    def canWalk(day: int) -> bool:
6      matrix = [[0] * col for _ in range(row)]
7      for i in range(day):
8        x, y = cells[i]
9        matrix[x - 1][y - 1] = 1
10
11      q = collections.deque()
12
13      for j in range(col):
14        if matrix[0][j] == 0:
15          q.append((0, j))
16          matrix[0][j] = 1
17
18      while q:
19        i, j = q.popleft()
20        for dx, dy in DIRS:
21          x = i + dx
22          y = j + dy
23          if x < 0 or x == row or y < 0 or y == col:
24            continue
25          if matrix[x][y] == 1:
26            continue
27          if x == row - 1:
28            return True
29          q.append((x, y))
30          matrix[x][y] = 1
31
32      return False
33
34    ans = 0
35    l = 1
36    r = len(cells) - 1
37
38    while l <= r:
39      m = (l + r) // 2
40      if canWalk(m):
41        ans = m
42        l = m + 1
43      else:
44        r = m - 1
45
46    return ans