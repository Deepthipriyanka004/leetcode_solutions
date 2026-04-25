// Last updated: 4/25/2026, 6:37:21 PM
1class Solution {
2  public int maxDistance(int side, int[][] points, int k) {
3    List<int[]> ordered = getOrderedPoints(side, points);
4    int l = 0;
5    int r = side;
6
7    while (l < r) {
8      final int m = (l + r + 1) / 2;
9      if (isValidDistance(ordered, k, m))
10        l = m;
11      else
12        r = m - 1;
13    }
14
15    return l;
16  }
17
18  private record Sequence(int startX, int startY, int endX, int endY, int length) {}
19
20  // Returns true if we can select `k` points such that the minimum Manhattan
21  // distance between any two consecutive chosen points is at least `m`.
22  private boolean isValidDistance(List<int[]> ordered, int k, int d) {
23    Deque<Sequence> dq = new ArrayDeque<>(List.of(new Sequence(
24        ordered.get(0)[0], ordered.get(0)[1], ordered.get(0)[0], ordered.get(0)[1], 1)));
25    int maxLength = 1;
26
27    for (int i = 1; i < ordered.size(); ++i) {
28      final int x = ordered.get(i)[0];
29      final int y = ordered.get(i)[1];
30      int startX = x;
31      int startY = y;
32      int length = 1;
33      while (!dq.isEmpty() &&
34             (Math.abs(x - dq.peekFirst().endX()) + Math.abs(y - dq.peekFirst().endY()) >= d)) {
35        if (Math.abs(x - dq.peekFirst().startX()) + Math.abs(y - dq.peekFirst().startY()) >= d &&
36            dq.peekFirst().length() + 1 >= length) {
37          startX = dq.peekFirst().startX();
38          startY = dq.peekFirst().startY();
39          length = dq.peekFirst().length() + 1;
40          maxLength = Math.max(maxLength, length);
41        }
42        dq.pollFirst();
43      }
44      dq.addLast(new Sequence(startX, startY, x, y, length));
45    }
46
47    return maxLength >= k;
48  }
49
50  // Returns the ordered points on the perimeter of a square of side length
51  // `side`, starting from left, top, right, and bottom boundaries.
52  private List<int[]> getOrderedPoints(int side, int[][] points) {
53    List<int[]> left = new ArrayList<>();
54    List<int[]> top = new ArrayList<>();
55    List<int[]> right = new ArrayList<>();
56    List<int[]> bottom = new ArrayList<>();
57
58    for (int[] point : points) {
59      final int x = point[0];
60      final int y = point[1];
61      if (x == 0 && y > 0)
62        left.add(point);
63      else if (x > 0 && y == side)
64        top.add(point);
65      else if (x == side && y < side)
66        right.add(point);
67      else
68        bottom.add(point);
69    }
70
71    left.sort(Comparator.comparingInt(a -> a[1]));
72    top.sort(Comparator.comparingInt(a -> a[0]));
73    right.sort(Comparator.comparingInt(a -> - a[1]));
74    bottom.sort(Comparator.comparingInt(a -> - a[0]));
75    List<int[]> ordered = new ArrayList<>();
76    ordered.addAll(left);
77    ordered.addAll(top);
78    ordered.addAll(right);
79    ordered.addAll(bottom);
80    return ordered;
81  }
82}