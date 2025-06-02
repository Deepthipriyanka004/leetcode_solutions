// Last updated: 6/2/2025, 6:32:02 PM
class Solution {
 public:
  long long coloredCells(int n) {
    return static_cast<long>(n) * n + static_cast<long>(n - 1) * (n - 1);
  }
};