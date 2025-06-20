// Last updated: 6/2/2025, 6:35:19 PM
class Solution {
 public:
  // Similar to 3. Longest Substring Without Repeating Characters
  int numberOfSubstrings(string s) {
    int ans = 0;
    vector<int> count(3);

    int l = 0;
    for (const char c : s) {
      ++count[c - 'a'];
      while (count[0] > 0 && count[1] > 0 && count[2] > 0)
        --count[s[l++] - 'a'];
      // s[0..r], s[1..r], ..., s[l - 1..r] are satified strings.
      ans += l;
    }

    return ans;
  }
};