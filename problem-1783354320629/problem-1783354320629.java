// Last updated: 7/6/2026, 9:42:00 PM
1class Solution {
2  public int removeCoveredIntervals(int[][] intervals) {
3    Arrays.sort(intervals, Comparator.comparingInt((int[] interval) -> interval[0])
4                               .thenComparingInt((int[] interval) -> - interval[1]));
5
6    int ans = 0;
7    int prevEnd = 0;
8
9    for (int[] interval : intervals)
10      // The current interval is not covered by the previous one.
11      if (prevEnd < interval[1]) {
12        prevEnd = interval[1];
13        ++ans;
14      }
15
16    return ans;
17  }
18}