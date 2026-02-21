// Last updated: 2/21/2026, 10:46:09 PM
1class Solution {
2 public:
3  int countPrimeSetBits(int left, int right) {
4    // {2, 3, 5, 7, 11, 13, 17, 19}-th bits are 1s.
5    // 0b10100010100010101100 = 665772
6    constexpr int magic = 665772;
7    int ans = 0;
8
9    for (unsigned num = left; num <= right; ++num)
10      if (magic >> popcount(num) & 1)
11        ++ans;
12
13    return ans;
14  }
15};
16
17
18