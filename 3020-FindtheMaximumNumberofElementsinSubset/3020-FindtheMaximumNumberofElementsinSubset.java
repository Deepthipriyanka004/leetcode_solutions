// Last updated: 6/27/2026, 11:31:59 AM
1class Solution {
2  public int maximumLength(int[] nums) {
3    final int maxNum = Arrays.stream(nums).max().getAsInt();
4    Map<Integer, Integer> count = new HashMap<>();
5
6    for (final int num : nums)
7      count.merge(num, 1, Integer::sum);
8
9    int ans = count.containsKey(1) ? count.get(1) - (count.get(1) % 2 == 0 ? 1 : 0) : 1;
10
11    for (final int num : nums) {
12      if (num == 1)
13        continue;
14      int length = 0;
15      long x = num;
16      while (x <= maxNum && count.containsKey((int) x) && count.get((int) x) >= 2) {
17        length += 2;
18        x *= x;
19      }
20      // x is now x^k, and the pattern is [x, ..., x^(k/2), x^(k/2), ..., x].
21      // The goal is to determine if we can insert x^k in the middle of the
22      // pattern to increase the length by 1. If not, we make x^(k/2) the middle
23      // and decrease the length by 1.
24      ans = Math.max(ans, length + (count.containsKey((int) x) ? 1 : -1));
25    }
26
27    return ans;
28  }
29}