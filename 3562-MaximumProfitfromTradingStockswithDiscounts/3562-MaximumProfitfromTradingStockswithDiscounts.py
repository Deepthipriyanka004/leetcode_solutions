# Last updated: 12/16/2025, 7:56:17 AM
1class Solution:
2  def maxProfit(
3      self,
4      n: int,
5      present: list[int],
6      future: list[int],
7      hierarchy: list[list[int]],
8      budget: int,
9  ) -> int:
10    tree = [[] for _ in range(n)]
11
12    for u, v in hierarchy:
13      tree[u - 1].append(v - 1)
14
15    @functools.lru_cache(None)
16    def dp(u: int, parent: int) -> tuple[list[int], list[int]]:
17      noDiscount = [0] * (budget + 1)
18      withDiscount = [0] * (budget + 1)
19
20      for v in tree[u]:
21        if v == parent:
22          continue
23        childNoDiscount, childWithDiscount = dp(v, u)
24        noDiscount = self._merge(noDiscount, childNoDiscount)
25        withDiscount = self._merge(withDiscount, childWithDiscount)
26
27      newDp0 = noDiscount[:]
28      newDp1 = noDiscount[:]
29
30      # 1. Buy current node at full cost (no discount)
31      fullCost = present[u]
32      for b in range(fullCost, budget + 1):
33        profit = future[u] - fullCost
34        newDp0[b] = max(newDp0[b], withDiscount[b - fullCost] + profit)
35
36      # 2. Buy current node at half cost (discounted by parent)
37      halfCost = present[u] // 2
38      for b in range(halfCost, budget + 1):
39        profit = future[u] - halfCost
40        newDp1[b] = max(newDp1[b], withDiscount[b - halfCost] + profit)
41
42      return newDp0, newDp1
43
44    return max(dp(0, -1)[0])
45
46  def _merge(self, dpA: list[int], dpB: list[int]) -> list[int]:
47    merged = [-math.inf] * len(dpA)
48    for i, a in enumerate(dpA):
49      for j in range(len(dpA) - i):
50        merged[i + j] = max(merged[i + j], a + dpB[j])
51    return merged