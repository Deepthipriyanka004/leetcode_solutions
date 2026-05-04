// Last updated: 5/4/2026, 11:38:47 PM
1class Solution {
2  public void rotate(int[][] matrix) {
3    for (int i = 0, j = matrix.length - 1; i < j; ++i, --j) {
4      int[] temp = matrix[i];
5      matrix[i] = matrix[j];
6      matrix[j] = temp;
7    }
8
9    for (int i = 0; i < matrix.length; ++i)
10      for (int j = i + 1; j < matrix.length; ++j) {
11        final int temp = matrix[i][j];
12        matrix[i][j] = matrix[j][i];
13        matrix[j][i] = temp;
14      }
15  }
16}