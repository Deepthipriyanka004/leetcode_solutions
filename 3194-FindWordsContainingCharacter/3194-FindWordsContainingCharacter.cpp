// Last updated: 6/2/2025, 6:31:06 PM
class Solution {
 public:
  vector<int> findWordsContaining(vector<string>& words, char x) {
    vector<int> ans;

    for (int i = 0; i < words.size(); ++i)
      if (words[i].find(x) != string::npos)
        ans.push_back(i);

    return ans;
  }
};