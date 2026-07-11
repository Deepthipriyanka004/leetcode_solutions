# Last updated: 7/11/2026, 8:49:50 PM
1class UnionFind:
2  def __init__(self, n: int):
3    self.id = list(range(n))
4    self.rank = [0] * n
5    self.nodeCount = [1] * n
6    self.edgeCount = [0] * n
7
8  def unionByRank(self, u: int, v: int) -> None:
9    i = self.find(u)
10    j = self.find(v)
11    self.edgeCount[i] += 1
12    if i == j:
13      return
14    if self.rank[i] < self.rank[j]:
15      self.id[i] = j
16      self.edgeCount[j] += self.edgeCount[i]
17      self.nodeCount[j] += self.nodeCount[i]
18    elif self.rank[i] > self.rank[j]:
19      self.id[j] = i
20      self.edgeCount[i] += self.edgeCount[j]
21      self.nodeCount[i] += self.nodeCount[j]
22    else:
23      self.id[i] = j
24      self.edgeCount[j] += self.edgeCount[i]
25      self.nodeCount[j] += self.nodeCount[i]
26      self.rank[j] += 1
27
28  def find(self, u: int) -> int:
29    if self.id[u] != u:
30      self.id[u] = self.find(self.id[u])
31    return self.id[u]
32
33  def isComplete(self, u):
34    return self.nodeCount[u] * (self.nodeCount[u] - 1) // 2 == self.edgeCount[u]
35
36
37class Solution:
38  def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
39    ans = 0
40    uf = UnionFind(n)
41    parents = set()
42
43    for u, v in edges:
44      uf.unionByRank(u, v)
45
46    for i in range(n):
47      parent = uf.find(i)
48      if parent not in parents and uf.isComplete(parent):
49        ans += 1
50        parents.add(parent)
51
52    return ans
53
54
55