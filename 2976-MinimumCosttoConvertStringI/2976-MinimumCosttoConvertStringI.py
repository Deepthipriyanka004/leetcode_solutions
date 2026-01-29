# Last updated: 1/29/2026, 9:57:53 AM
1class Solution:
2  def minimumCost(
3      self,
4      source: str,
5      target: str,
6      original: list[str],
7      changed: list[str],
8      cost: list[int],
9  ) -> int:
10    ans = 0
11    # dist[u][v] := the minimum distance to change ('a' + u) to ('a' + v)
12    dist = [[math.inf] * 26 for _ in range(26)]
13
14    for a, b, c in zip(original, changed, cost):
15      u = ord(a) - ord('a')
16      v = ord(b) - ord('a')
17      dist[u][v] = min(dist[u][v], c)
18
19    for k in range(26):
20      for i in range(26):
21        if dist[i][k] < math.inf:
22          for j in range(26):
23            if dist[k][j] < math.inf:
24              dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
25
26    for s, t in zip(source, target):
27      if s == t:
28        continue
29      u = ord(s) - ord('a')
30      v = ord(t) - ord('a')
31      if dist[u][v] == math.inf:
32        return -1
33      ans += dist[u][v]
34
35    return ans
36
37
38