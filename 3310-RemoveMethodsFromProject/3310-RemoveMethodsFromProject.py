# Last updated: 8/5/2026, 7:18:47 PM
1class Solution:
2  def remainingMethods(
3      self,
4      n: int,
5      k: int,
6      invocations: list[list[int]]
7  ) -> list[int]:
8    ans = []
9    graph = [[] for _ in range(n)]
10
11    for u, v in invocations:
12      graph[u].append(v)
13
14    q = collections.deque([k])
15    seen = {k}
16
17    while q:
18      for _ in range(len(q)):
19        for v in graph[q.popleft()]:
20          if v not in seen:
21            q.append(v)
22            seen.add(v)
23
24    for u in range(n):
25      if u in seen:
26        continue
27      for v in graph[u]:
28        if v in seen:
29          return list(range(n))
30      ans.append(u)
31
32    return ans
33
34
35