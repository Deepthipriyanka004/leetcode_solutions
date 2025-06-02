// Last updated: 6/2/2025, 6:42:09 PM
class Solution {
 public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    vector<vector<string>> ans;
    unordered_map<string, vector<string>> keyToAnagrams;

    for (const string& str : strs) {
      string key = str;
      ranges::sort(key);
      keyToAnagrams[key].push_back(str);
    }

    for (const auto& [_, anagrams] : keyToAnagrams)
      ans.push_back(anagrams);

    return ans;
  }
};