// Last updated: 6/2/2025, 6:36:30 PM
class Solution {
 public:
  vector<string> uncommonFromSentences(string A, string B) {
    vector<string> ans;
    unordered_map<string, int> count;
    istringstream iss(A + ' ' + B);

    while (iss >> A)
      ++count[A];

    for (const auto& [word, freq] : count)
      if (freq == 1)
        ans.push_back(word);

    return ans;
  }
};