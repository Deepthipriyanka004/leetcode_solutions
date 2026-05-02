// Last updated: 5/2/2026, 10:57:16 AM
1class Solution {
2 public:
3  int rotatedDigits(int n) {
4    int ans = 0;
5
6    for (int i = 1; i <= n; ++i)
7      if (isGoodNumber(i))
8        ++ans;
9
10    return ans;
11  }
12
13 private:
14  bool isGoodNumber(int i) {
15    bool isRotated = false;
16
17    for (const char c : to_string(i)) {
18      if (c == '0' || c == '1' || c == '8')
19        continue;
20      if (c == '2' || c == '5' || c == '6' || c == '9')
21        isRotated = true;
22      else
23        return false;
24    }
25
26    return isRotated;
27  }
28};