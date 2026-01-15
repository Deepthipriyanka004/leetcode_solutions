// Last updated: 1/15/2026, 12:37:29 PM
1class Solution {
2 public:
3  int maximizeSquareHoleArea(int n, int m, vector<int>& hBars,
4                             vector<int>& vBars) {
5    const int gap = min(maxContinousGap(hBars), maxContinousGap(vBars));
6    return gap * gap;
7  }
8
9 private:
10  int maxContinousGap(vector<int>& bars) {
11    int res = 2;
12    int runningGap = 2;
13    ranges::sort(bars);
14    for (int i = 1; i < bars.size(); ++i) {
15      runningGap = bars[i] == bars[i - 1] + 1 ? runningGap + 1 : 2;
16      res = max(res, runningGap);
17    }
18    return res;
19  }
20};