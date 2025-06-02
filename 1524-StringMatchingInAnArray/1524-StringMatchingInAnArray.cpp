// Last updated: 6/2/2025, 6:35:02 PM
class Solution {
 public:
  vector<string> stringMatching(vector<string>& words) {
    vector<string> ans;
    for (const string& a : words)
      for (const string& b : words)
        if (a.length() < b.length() && b.find(a) != string::npos) {
          ans.push_back(a);
          break;
        }
    return ans;
  }
};