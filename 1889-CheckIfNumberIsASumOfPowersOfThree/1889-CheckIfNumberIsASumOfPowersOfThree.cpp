// Last updated: 6/2/2025, 6:34:28 PM
class Solution {
 public:
  bool checkPowersOfThree(int n) {
    while (n > 1) {
      const int r = n % 3;
      if (r == 2)
        return false;
      n /= 3;
    }

    return true;
  }
};