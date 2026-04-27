// Last updated: 4/27/2026, 12:32:34 PM
1class Solution {
2  public boolean hasValidPath(int[][] grid) {
3    final int m = grid.length;
4    final int n = grid[0].length;
5    // g := upscaled grid
6    boolean[][] g = new boolean[m * 3][n * 3];
7
8    for (int i = 0; i < m; ++i)
9      for (int j = 0; j < n; ++j)
10        switch (grid[i][j]) {
11          case 1:
12            g[i * 3 + 1][j * 3 + 0] = true;
13            g[i * 3 + 1][j * 3 + 1] = true;
14            g[i * 3 + 1][j * 3 + 2] = true;
15            break;
16          case 2:
17            g[i * 3 + 0][j * 3 + 1] = true;
18            g[i * 3 + 1][j * 3 + 1] = true;
19            g[i * 3 + 2][j * 3 + 1] = true;
20            break;
21          case 3:
22            g[i * 3 + 1][j * 3 + 0] = true;
23            g[i * 3 + 1][j * 3 + 1] = true;
24            g[i * 3 + 2][j * 3 + 1] = true;
25            break;
26          case 4:
27            g[i * 3 + 1][j * 3 + 1] = true;
28            g[i * 3 + 1][j * 3 + 2] = true;
29            g[i * 3 + 2][j * 3 + 1] = true;
30            break;
31          case 5:
32            g[i * 3 + 0][j * 3 + 1] = true;
33            g[i * 3 + 1][j * 3 + 0] = true;
34            g[i * 3 + 1][j * 3 + 1] = true;
35            break;
36          case 6:
37            g[i * 3 + 0][j * 3 + 1] = true;
38            g[i * 3 + 1][j * 3 + 1] = true;
39            g[i * 3 + 1][j * 3 + 2] = true;
40            break;
41        }
42
43    return dfs(g, 1, 1);
44  }
45
46  private boolean dfs(boolean[][] g, int i, int j) {
47    if (i < 0 || i == g.length || j < 0 || j == g[0].length)
48      return false;
49    if (!g[i][j]) // There's no path here.
50      return false;
51    if (i == g.length - 2 && j == g[0].length - 2)
52      return true;
53
54    g[i][j] = false; // Mark as visited.
55    return dfs(g, i + 1, j) || dfs(g, i - 1, j) || dfs(g, i, j + 1) || dfs(g, i, j - 1);
56  }
57}
58