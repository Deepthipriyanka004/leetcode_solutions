// Last updated: 1/3/2026, 10:51:38 AM
1class Solution {
2 public:
3  int numOfWays(int n) {
4    constexpr int kMod = 1'000'000'007;
5    long color2 = 6;  // 121, 131, 212, 232, 313, 323
6    long color3 = 6;  // 123, 132, 213, 231, 312, 321
7
8    for (int i = 1; i < n; ++i) {
9      const long nextColor2 = color2 * 3 + color3 * 2;
10      const long nextColor3 = color2 * 2 + color3 * 2;
11      color2 = nextColor2 % kMod;
12      color3 = nextColor3 % kMod;
13    }
14
15    return (color2 + color3) % kMod;
16  }
17};