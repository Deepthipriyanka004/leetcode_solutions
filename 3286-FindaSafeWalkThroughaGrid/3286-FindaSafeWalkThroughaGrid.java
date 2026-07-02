// Last updated: 7/2/2026, 9:25:05 PM
1class Solution {
2  public boolean findSafeWalk(List<List<Integer>> grid, int health) {
3    record T(int i, int j, int h) {}
4    final int[][] DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
5    final int m = grid.size();
6    final int n = grid.get(0).size();
7    final int initialHealth = health - grid.get(0).get(0);
8    Queue<T> q = new ArrayDeque<>(List.of(new T(0, 0, initialHealth)));
9    boolean[][][] seen = new boolean[m][n][health + 1];
10    seen[0][0][initialHealth] = true;
11
12    while (!q.isEmpty())
13      for (int sz = q.size(); sz > 0; --sz) {
14        final int i = q.peek().i;
15        final int j = q.peek().j;
16        final int h = q.poll().h;
17        if (i == m - 1 && j == n - 1 && h > 0)
18          return true;
19        for (int k = 0; k < 4; ++k) {
20          final int x = i + DIRS[k][0];
21          final int y = j + DIRS[k][1];
22          if (x < 0 || x == m || y < 0 || y == n)
23            continue;
24          final int nextHealth = h - grid.get(x).get(y);
25          if (nextHealth <= 0 || seen[x][y][nextHealth])
26            continue;
27          q.offer(new T(x, y, nextHealth));
28          seen[x][y][nextHealth] = true;
29        }
30      }
31
32    return false;
33  }
34}