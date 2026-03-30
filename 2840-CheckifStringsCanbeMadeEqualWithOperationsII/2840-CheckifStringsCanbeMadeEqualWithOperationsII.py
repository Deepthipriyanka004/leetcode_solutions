# Last updated: 3/30/2026, 8:55:22 AM
1class Solution:
2  def checkStrings(self, s1: str, s2: str) -> bool:
3    count = [collections.Counter() for _ in range(2)]
4
5    for i, (a, b) in enumerate(zip(s1, s2)):
6      count[i % 2][a] += 1
7      count[i % 2][b] -= 1
8
9    return (all(freq == 0 for freq in count[0].values()) and
10            all(freq == 0 for freq in count[1].values()))