// Last updated: 7/1/2026, 7:12:10 AM
1class Solution {
2  public int maximumSafenessFactor(List<List<Integer>> grid) {
3    int[][] distToThief = getDistToThief(grid);
4    int l = 0;
5    int r = grid.size() * 2;
6
7    while (l < r) {
8      final int m = (l + r) / 2;
9      if (hasValidPath(distToThief, m))
10        l = m + 1;
11      else
12        r = m;
13    }
14
15    return l - 1;
16  }
17
18  private static final int[][] DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
19
20  private boolean hasValidPath(int[][] distToThief, int safeness) {
21    if (distToThief[0][0] < safeness)
22      return false;
23
24    final int n = distToThief.length;
25    Queue<Pair<Integer, Integer>> q = new ArrayDeque<>(List.of(new Pair<>(0, 0)));
26    boolean[][] seen = new boolean[n][n];
27    seen[0][0] = true;
28
29    while (!q.isEmpty()) {
30      final int i = q.peek().getKey();
31      final int j = q.poll().getValue();
32      if (distToThief[i][j] < safeness)
33        continue;
34      if (i == n - 1 && j == n - 1)
35        return true;
36      for (int[] dir : DIRS) {
37        final int x = i + dir[0];
38        final int y = j + dir[1];
39        if (x < 0 || x == n || y < 0 || y == n)
40          continue;
41        if (seen[x][y])
42          continue;
43        q.offer(new Pair<>(x, y));
44        seen[x][y] = true;
45      }
46    }
47
48    return false;
49  }
50
51  private int[][] getDistToThief(List<List<Integer>> grid) {
52    final int n = grid.size();
53    int[][] distToThief = new int[n][n];
54    Queue<Pair<Integer, Integer>> q = new ArrayDeque<>();
55    boolean[][] seen = new boolean[n][n];
56
57    for (int i = 0; i < n; ++i)
58      for (int j = 0; j < n; ++j)
59        if (grid.get(i).get(j) == 1) {
60          q.offer(new Pair<>(i, j));
61          seen[i][j] = true;
62        }
63
64    for (int dist = 0; !q.isEmpty(); ++dist) {
65      for (int sz = q.size(); sz > 0; --sz) {
66        final int i = q.peek().getKey();
67        final int j = q.poll().getValue();
68        distToThief[i][j] = dist;
69        for (int[] dir : DIRS) {
70          final int x = i + dir[0];
71          final int y = j + dir[1];
72          if (x < 0 || x == n || y < 0 || y == n)
73            continue;
74          if (seen[x][y])
75            continue;
76          q.offer(new Pair<>(x, y));
77          seen[x][y] = true;
78        }
79      }
80    }
81
82    return distToThief;
83  }
84}