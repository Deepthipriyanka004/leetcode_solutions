// Last updated: 5/6/2026, 9:13:49 PM
1class Solution {
2  public char[][] rotateTheBox(char[][] box) {
3    final int m = box.length;
4    final int n = box[0].length;
5    char[][] ans = new char[n][m];
6    Arrays.stream(ans).forEach(A -> Arrays.fill(A, '.'));
7
8    for (int i = 0; i < m; ++i)
9      for (int j = n - 1, k = n - 1; j >= 0; --j)
10        if (box[i][j] != '.') {
11          if (box[i][j] == '*')
12            k = j;
13          ans[k--][m - i - 1] = box[i][j];
14        }
15
16    return ans;
17  }
18}
19