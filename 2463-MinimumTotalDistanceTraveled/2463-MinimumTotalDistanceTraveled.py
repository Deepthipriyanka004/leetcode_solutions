# Last updated: 4/14/2026, 9:40:27 AM
1class Solution:
2  def minimumTotalDistance(
3      self,
4      robot: list[int],
5      factory: list[list[int]],
6  ) -> int:
7    robot.sort()
8    factory.sort()
9
10    @functools.lru_cache(None)
11    def dp(i: int, j: int, k: int) -> int:
12      """
13      Returns the minimum distance to fix robot[i..n) with factory[j..n), where
14      factory[j] already fixed k robots.
15      """
16      if i == len(robot):
17        return 0
18      if j == len(factory):
19        return math.inf
20      skipFactory = dp(i, j + 1, 0)
21      position, limit = factory[j]
22      useFactory = (dp(i + 1, j, k + 1) + abs(robot[i] - position)
23                    if limit > k else math.inf)
24      return min(skipFactory, useFactory)
25
26    return dp(0, 0, 0)