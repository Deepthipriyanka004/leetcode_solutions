// Last updated: 8/3/2026, 8:08:29 PM
1class Solution {
2  public String stoneGameIII(int[] stoneValue) {
3    int[] mem = new int[stoneValue.length];
4    Arrays.fill(mem, Integer.MIN_VALUE);
5    final int score = stoneGameIII(stoneValue, 0, mem);
6    return score > 0 ? "Alice" : score < 0 ? "Bob" : "Tie";
7  }
8
9  // Returns the maximum relative score Alice can make from stoneValue[i..n).
10  private int stoneGameIII(int[] stoneValue, int i, int[] mem) {
11    if (i == stoneValue.length)
12      return 0;
13    if (mem[i] > Integer.MIN_VALUE)
14      return mem[i];
15
16    int sum = 0;
17    for (int j = i; j < i + 3 && j < stoneValue.length; ++j) {
18      sum += stoneValue[j];
19      mem[i] = Math.max(mem[i], sum - stoneGameIII(stoneValue, j + 1, mem));
20    }
21
22    return mem[i];
23  };
24}