// Last updated: 7/7/2026, 7:25:48 PM
1class Solution {
2    public long sumAndMultiply(int n) {
3        int p = 1;
4        int x = 0, s = 0;
5        for (; n > 0; n /= 10) {
6            int v = n % 10;
7            if (v != 0) {
8                s += v;
9                x += p * v;
10                p *= 10;
11            }
12        }
13        return 1L * x * s;
14    }
15}