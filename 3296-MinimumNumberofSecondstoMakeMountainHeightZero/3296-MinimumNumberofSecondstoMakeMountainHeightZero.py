# Last updated: 3/13/2026, 10:24:33 PM
1class Solution:
2  def minNumberOfSeconds(
3      self,
4      mountainHeight: int,
5      workerTimes: list[int]
6  ) -> int:
7    def getReducedHeight(m: int) -> int:
8      """Returns the total height reduced by all workers in `m` seconds."""
9      # The height `x` that a worker with working time `w` reduces in `m`
10      # seconds.
11      # w * (1 + 2 + ... + x) <= m
12      #       (1 + x) * x / 2 <= m / w
13      #   x^2 + x - 2 * m / w <= 0
14      #                     x <= (-1 + sqrt(1 + 8 * m / w)) / 2
15      return sum((-1 + math.sqrt(1 + 8 * m // workerTime)) // 2
16                 for workerTime in workerTimes)
17
18    l = 1
19    r = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
20    return bisect.bisect_left(range(l, r), mountainHeight,
21                              key=getReducedHeight) + l