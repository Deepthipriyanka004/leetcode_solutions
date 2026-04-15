// Last updated: 4/15/2026, 9:37:16 AM
1class Solution {
2public:
3    int closestTarget(vector<string>& words, string target, int startIndex) {
4        int n = words.size();
5
6        for (int i = 0; i < n; ++i) {
7            // forward direction
8            if (words[(startIndex + i) % n] == target)
9                return i;
10
11            // backward direction
12            if (i > 0 && words[(startIndex - i + n) % n] == target)
13                return i;
14        }
15
16        return -1;
17    }
18};