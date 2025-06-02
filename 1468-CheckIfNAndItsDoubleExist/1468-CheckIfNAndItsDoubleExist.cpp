// Last updated: 6/2/2025, 6:35:16 PM
class Solution {
 public:
  bool checkIfExist(vector<int>& arr) {
    unordered_set<int> seen;

    for (const int a : arr) {
      if (seen.contains(a * 2) || a % 2 == 0 && seen.contains(a / 2))
        return true;
      seen.insert(a);
    }

    return false;
  }
};