// Last updated: 6/2/2025, 6:35:51 PM
class Solution {
 public:
  bool threeConsecutiveOdds(vector<int>& arr) {
    int count = 0;
    for (const int a : arr) {
      count = a % 2 == 1 ? count + 1 : 0;
      if (count == 3)
        return true;
    }
    return false;
  }
};