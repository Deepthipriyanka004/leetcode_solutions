// Last updated: 6/2/2025, 6:31:11 PM
class Solution {
 public:
  int minChanges(string s) {
    int ans = 0;

    for (int i = 0; i + 1 < s.length(); i += 2)
      if (s[i] != s[i + 1])
        ++ans;

    return ans;
  }
};