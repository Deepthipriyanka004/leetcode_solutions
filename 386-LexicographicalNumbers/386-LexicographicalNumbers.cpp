// Last updated: 6/2/2025, 6:37:28 PM
class Solution {
 public:
  vector<int> lexicalOrder(int n) {
    vector<int> ans;
    int curr = 1;

    while (ans.size() < n) {
      ans.push_back(curr);
      if (curr * 10 <= n) {
        curr *= 10;
      } else {
        while (curr % 10 == 9 || curr == n)
          curr /= 10;
        ++curr;
      }
    }

    return ans;
  }
};