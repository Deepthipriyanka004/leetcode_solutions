// Last updated: 6/2/2025, 6:35:36 PM
class Solution {
 public:
  vector<string> removeSubfolders(vector<string>& folder) {
    vector<string> ans;
    string prev;

    ranges::sort(folder);

    for (const string& f : folder) {
      if (!prev.empty() && f.find(prev) == 0 && f[prev.length()] == '/')
        continue;
      ans.push_back(f);
      prev = f;
    }

    return ans;
  }
};