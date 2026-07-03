# Last updated: 7/3/2026, 9:06:12 PM
1class Solution:
2    def findMaxPathScore(
3        self, edges: List[List[int]], online: List[bool], k: int
4    ) -> int:
5        def check(mid: int) -> int:
6            dist = [inf] * n
7            dist[0] = 0
8            pq = [(0, 0)]
9            while pq:
10                d, u = heappop(pq)
11                if d > k:
12                    return False
13                if u == n - 1:
14                    return True
15                if dist[u] < d:
16                    continue
17                for v, w in g[u]:
18                    if w < mid:
19                        continue
20                    if dist[u] + w < dist[v]:
21                        dist[v] = dist[u] + w
22                        heappush(pq, (dist[v], v))
23            return False
24
25        n = len(online)
26        g = [[] for _ in range(n)]
27        l, r = inf, 0
28        for (
29            u,
30            v,
31            w,
32        ) in edges:
33            if not online[u] or not online[v]:
34                continue
35            g[u].append((v, w))
36            l = min(l, w)
37            r = max(r, w)
38
39        while l < r:
40            mid = (l + r + 1) >> 1
41            if check(mid):
42                l = mid
43            else:
44                r = mid - 1
45        return l if check(l) else -1