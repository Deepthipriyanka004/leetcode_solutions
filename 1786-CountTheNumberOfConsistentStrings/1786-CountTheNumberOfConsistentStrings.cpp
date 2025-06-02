// Last updated: 6/2/2025, 6:34:36 PM
class Solution {
 public:
  int countConsistentStrings(string allowed, vector<string>& words) {
    return accumulate(words.begin(), words.end(), 0,
                      [&allowed](int subtotal, const string& word) {
      return subtotal + ranges::all_of(word, [&allowed](char c) {
        return allowed.find(c) != string::npos;
      });
    });
  }
};