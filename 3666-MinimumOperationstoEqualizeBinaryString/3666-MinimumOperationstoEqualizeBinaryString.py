# Last updated: 2/27/2026, 6:46:49 PM
1class Solution:
2    def minOperations(self, s: str, k: int) -> int:
3        n = len(s)
4        ts = [SortedSet() for _ in range(2)]
5        for i in range(n + 1):
6            ts[i % 2].add(i)
7        cnt0 = s.count('0')
8        ts[cnt0 % 2].remove(cnt0)
9        q = deque([cnt0])
10        ans = 0
11        while q:
12            for _ in range(len(q)):
13                cur = q.popleft()
14                if cur == 0:
15                    return ans
16                l = cur + k - 2 * min(cur, k)
17                r = cur + k - 2 * max(k - n + cur, 0)
18                t = ts[l % 2]
19                j = t.bisect_left(l)
20                while j < len(t) and t[j] <= r:
21                    q.append(t[j])
22                    t.remove(t[j])
23            ans += 1
24        return -1