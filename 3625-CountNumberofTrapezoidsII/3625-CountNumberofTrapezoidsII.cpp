// Last updated: 12/3/2025, 9:12:24 PM
1class Solution {
2public:
3    int countTrapezoids(vector<vector<int>>& points) {
4        int n = points.size();
5        unordered_map<double, unordered_map<double, int>> cnt1;
6        unordered_map<int, unordered_map<double, int>> cnt2;
7
8        cnt1.reserve(n * n);
9        cnt2.reserve(n * n);
10
11        for (int i = 0; i < n; ++i) {
12            int x1 = points[i][0], y1 = points[i][1];
13            for (int j = 0; j < i; ++j) {
14                int x2 = points[j][0], y2 = points[j][1];
15                int dx = x2 - x1, dy = y2 - y1;
16                double k = (dx == 0 ? 1e9 : 1.0 * dy / dx);
17                double b = (dx == 0 ? x1 : 1.0 * (1LL * y1 * dx - 1LL * x1 * dy) / dx);
18
19                cnt1[k][b] += 1;
20                int p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000);
21                cnt2[p][k] += 1;
22            }
23        }
24
25        int ans = 0;
26        for (auto& [_, e] : cnt1) {
27            int s = 0;
28            for (auto& [_, t] : e) {
29                ans += s * t;
30                s += t;
31            }
32        }
33        for (auto& [_, e] : cnt2) {
34            int s = 0;
35            for (auto& [_, t] : e) {
36                ans -= s * t;
37                s += t;
38            }
39        }
40        return ans;
41    }
42};
43