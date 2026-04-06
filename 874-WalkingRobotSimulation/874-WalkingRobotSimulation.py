# Last updated: 4/6/2026, 12:07:10 PM
1class Solution:
2  def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
3    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
4    ans = 0
5    d = 0  # 0 := north, 1 := east, 2 := south, 3 := west
6    x = 0  # the start x
7    y = 0  # the start y
8    obstaclesSet = {(x, y) for x, y in obstacles}
9
10    for command in commands:
11      if command == -1:
12        d = (d + 1) % 4
13      elif command == -2:
14        d = (d + 3) % 4
15      else:
16        for _ in range(command):
17          if (x + DIRS[d][0], y + DIRS[d][1]) in obstaclesSet:
18            break
19          x += DIRS[d][0]
20          y += DIRS[d][1]
21      ans = max(ans, x * x + y * y)
22
23    return ans