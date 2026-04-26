// Last updated: 4/26/2026, 9:33:23 AM
1class Solution {
2  public boolean containsCycle(char[][] grid) {
3    final int m = grid.length;
4    final int n = grid[0].length;
5    boolean[][] seen = new boolean[m][n];
6
7    for (int i = 0; i < m; ++i)
8      for (int j = 0; j < n; ++j) {
9        if (seen[i][j])
10          continue;
11        if (dfs(grid, i, j, -1, -1, grid[i][j], seen))
12          return true;
13      }
14
15    return false;
16  }
17
18  private static final int[][] DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
19
20  private boolean dfs(char[][] grid, int i, int j, int prevI, int prevJ, char c, boolean[][] seen) {
21    seen[i][j] = true;
22
23    for (int[] dir : DIRS) {
24      final int x = i + dir[0];
25      final int y = j + dir[1];
26      if (x < 0 || x == grid.length || y < 0 || y == grid[0].length)
27        continue;
28      if (x == prevI && y == prevJ)
29        continue;
30      if (grid[x][y] != c)
31        continue;
32      if (seen[x][y])
33        return true;
34      if (dfs(grid, x, y, i, j, c, seen))
35        return true;
36    }
37
38    return false;
39  }
40}