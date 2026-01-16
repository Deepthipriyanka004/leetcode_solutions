// Last updated: 1/16/2026, 10:22:31 AM
1class Solution {
2 public:
3  int maximizeSquareArea(int m, int n, vector<int>& hFences,
4                         vector<int>& vFences) {
5    constexpr int kMod = 1'000'000'007;
6
7    hFences.push_back(1);
8    hFences.push_back(m);
9    vFences.push_back(1);
10    vFences.push_back(n);
11
12    ranges::sort(hFences);
13    ranges::sort(vFences);
14
15    const unordered_set<int> hGaps = getGaps(hFences);
16    const unordered_set<int> vGaps = getGaps(vFences);
17    int maxGap = -1;
18
19    for (const int hGap : hGaps)
20      if (vGaps.contains(hGap))
21        maxGap = max(maxGap, hGap);
22
23    return maxGap == -1 ? -1 : static_cast<long>(maxGap) * maxGap % kMod;
24  }
25
26 private:
27  unordered_set<int> getGaps(const vector<int>& fences) {
28    unordered_set<int> gaps;
29    for (int i = 0; i < fences.size(); ++i)
30      for (int j = 0; j < i; ++j)
31        gaps.insert(fences[i] - fences[j]);
32    return gaps;
33  }
34};