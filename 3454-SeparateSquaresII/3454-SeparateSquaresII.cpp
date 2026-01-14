// Last updated: 1/14/2026, 1:56:38 PM
1class SegmentTree {
2 public:
3  explicit SegmentTree(const vector<int>& xs)
4      : xs(xs), n(xs.size() - 1), coveredCount(4 * n), coveredWidth(4 * n) {}
5
6  // Adds val to the range [i, j].
7  void add(int i, int j, int val) {
8    add(0, 0, n - 1, i, j, val);
9  }
10
11  // Returns the covered width of xs[0..n - 1].
12  int getCoveredWidth() const {
13    return coveredWidth[0];
14  }
15
16 private:
17  const int n;  // the number of segments (|xs| - 1)
18  vector<int> xs;
19  vector<int> coveredCount;
20  vector<int> coveredWidth;
21
22  void add(int treeIndex, int lo, int hi, int i, int j, int val) {
23    if (j <= xs[lo] || xs[hi + 1] <= i)
24      return;
25    if (i <= xs[lo] && xs[hi + 1] <= j) {
26      coveredCount[treeIndex] += val;
27    } else {
28      const int mid = (lo + hi) / 2;
29      add(2 * treeIndex + 1, lo, mid, i, j, val);
30      add(2 * treeIndex + 2, mid + 1, hi, i, j, val);
31    }
32    if (coveredCount[treeIndex] > 0) {
33      coveredWidth[treeIndex] = xs[hi + 1] - xs[lo];
34    } else if (lo == hi) {
35      coveredWidth[treeIndex] = 0;
36    } else {
37      coveredWidth[treeIndex] =
38          coveredWidth[2 * treeIndex + 1] + coveredWidth[2 * treeIndex + 2];
39    }
40  }
41};
42
43class Solution {
44 public:
45  double separateSquares(vector<vector<int>>& squares) {
46    vector<tuple<int, int, int, int>> events;  // (y, delta, xl, xr)
47    set<int> xs;
48
49    for (const vector<int>& square : squares) {
50      const int x = square[0];
51      const int y = square[1];
52      const int l = square[2];
53      events.emplace_back(y, 1, x, x + l);
54      events.emplace_back(y + l, -1, x, x + l);
55      xs.insert(x);
56      xs.insert(x + l);
57    }
58
59    ranges::sort(events);
60
61    const double halfArea = getArea(events, xs) / 2.0;
62    long area = 0;
63    int prevY = 0;
64    SegmentTree tree({xs.begin(), xs.end()});
65
66    for (const auto& [y, delta, xl, xr] : events) {
67      const int coveredWidth = tree.getCoveredWidth();
68      const long areaGain = coveredWidth * static_cast<long>(y - prevY);
69      if (area + areaGain >= halfArea)
70        return prevY + (halfArea - area) / coveredWidth;
71      area += areaGain;
72      tree.add(xl, xr, delta);
73      prevY = y;
74    }
75
76    throw;
77  }
78
79 private:
80  // Returns the total area of the rectangles.
81  long getArea(const vector<tuple<int, int, int, int>>& events,
82               const set<int>& xs) {
83    long totalArea = 0;
84    int prevY = 0;
85    SegmentTree tree({xs.begin(), xs.end()});
86    for (const auto& [y, delta, xl, xr] : events) {
87      totalArea += tree.getCoveredWidth() * static_cast<long>(y - prevY);
88      tree.add(xl, xr, delta);
89      prevY = y;
90    }
91    return totalArea;
92  }
93};
94
95
96