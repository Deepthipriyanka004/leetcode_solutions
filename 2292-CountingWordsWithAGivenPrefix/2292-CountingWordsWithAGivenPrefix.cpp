// Last updated: 6/2/2025, 6:33:08 PM
class Solution {
 public:
  int prefixCount(vector<string>& words, string pref) {
    return ranges::count_if(
        words, [&](const string& word) { return word.find(pref) == 0; });
  }
};