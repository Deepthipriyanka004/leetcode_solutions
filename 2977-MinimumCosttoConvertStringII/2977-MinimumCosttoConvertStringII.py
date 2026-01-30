# Last updated: 1/30/2026, 1:38:44 PM
1class Solution:
2  def minimumCost(
3      self,
4      source: str,
5      target: str,
6      original: list[str],
7      changed: list[str],
8      cost: list[int],
9  ) -> int:
10    subLengths = set(len(s) for s in original)
11    subToId = self._getSubToId(original, changed)
12    subCount = len(subToId)
13    # dist[u][v] := the minimum distance to change the substring with id u to
14    # the substring with id v
15    dist = [[math.inf for _ in range(subCount)] for _ in range(subCount)]
16    # dp[i] := the minimum cost to change the first i letters of `source` into
17    # `target`, leaving the suffix untouched
18    dp = [math.inf for _ in range(len(source) + 1)]
19
20    for a, b, c in zip(original, changed, cost):
21      u = subToId[a]
22      v = subToId[b]
23      dist[u][v] = min(dist[u][v], c)
24
25    for k in range(subCount):
26      for i in range(subCount):
27        if dist[i][k] < math.inf:
28          for j in range(subCount):
29            if dist[k][j] < math.inf:
30              dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
31
32    dp[0] = 0
33
34    for i, (s, t) in enumerate(zip(source, target)):
35      if dp[i] == math.inf:
36        continue
37      if s == t:
38        dp[i + 1] = min(dp[i + 1], dp[i])
39      for subLength in subLengths:
40        if i + subLength > len(source):
41          continue
42        subSource = source[i:i + subLength]
43        subTarget = target[i:i + subLength]
44        if subSource not in subToId or subTarget not in subToId:
45          continue
46        u = subToId[subSource]
47        v = subToId[subTarget]
48        if dist[u][v] != math.inf:
49          dp[i + subLength] = min(dp[i + subLength], dp[i] + dist[u][v])
50
51    return -1 if dp[len(source)] == math.inf else dp[len(source)]
52
53  def _getSubToId(self, original: str, changed: str) -> dict[str, int]:
54    subToId = {}
55    for s in original + changed:
56      if s not in subToId:
57        subToId[s] = len(subToId)
58    return subToId
59
60
61