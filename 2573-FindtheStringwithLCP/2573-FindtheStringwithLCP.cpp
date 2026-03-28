// Last updated: 3/28/2026, 7:37:47 PM
1class Solution {
2 public:
3  string findTheString(vector<vector<int>>& lcp) {
4    const int n = lcp.size();
5    constexpr char nonLetter = 'a' - 1;
6    char c = nonLetter;
7    vector<char> word(n, nonLetter);
8
9    for (int i = 0; i < n; ++i) {
10      if (word[i] != nonLetter)  // There's a candidate already.
11        continue;
12      if (++c > 'z')  // Run out of letters, so return "".
13        return "";
14      // No need to consider [0..i - 1] since they were considered.
15      for (int j = i; j < n; ++j)
16        if (lcp[i][j] > 0)
17          word[j] = c;
18    }
19
20    // Check if `word` is valid.
21    for (int i = 0; i < n; ++i)
22      for (int j = 0; j < n; ++j) {
23        const int nextLcp = i + 1 < n && j + 1 < n ? lcp[i + 1][j + 1] : 0;
24        const int currLcp = word[i] == word[j] ? 1 + nextLcp : 0;
25        if (lcp[i][j] != currLcp)
26          return "";
27      }
28
29    string ans;
30    for (const char c : word)
31      ans += c;
32    return ans;
33  }
34};
35