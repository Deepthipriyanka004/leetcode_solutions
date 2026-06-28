// Last updated: 6/28/2026, 10:36:38 AM
1class Solution {
2  public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
3    Arrays.sort(arr);
4    arr[0] = 1;
5
6    for (int i = 1; i < arr.length; ++i)
7      arr[i] = Math.min(arr[i], arr[i - 1] + 1);
8
9    return arr[arr.length - 1];
10  }
11}
12
13
14