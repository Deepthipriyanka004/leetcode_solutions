# Last updated: 5/12/2026, 9:38:21 PM
1class Solution:
2  def minimumEffort(self, tasks: list[list[int]]) -> int:
3    ans = 0
4    prevSaved = 0
5
6    for actual, minimum in sorted(tasks, key=lambda x: x[0] - x[1]):
7      if prevSaved < minimum:
8        ans += minimum - prevSaved
9        prevSaved = minimum - actual
10      else:
11        prevSaved -= actual
12
13    return ans