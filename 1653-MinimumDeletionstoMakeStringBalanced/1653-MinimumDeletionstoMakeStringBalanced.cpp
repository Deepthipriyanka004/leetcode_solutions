// Last updated: 2/7/2026, 5:32:11 PM
1class Solution {
2 public:
3  // Same as 926. Flip String to Monotone Increasing
4  int minimumDeletions(string s) {
5    // the number of characters to be deleted to make the substring so far
6    // balanced
7    int dp = 0;
8    int countB = 0;
9
10    for (const char c : s)
11      if (c == 'a')
12        // 1. Delete 'a'.
13        // 2. Keep 'a' and delete the previous 'b's.
14        dp = min(dp + 1, countB);
15      else
16        ++countB;
17
18    return dp;
19  }
20};