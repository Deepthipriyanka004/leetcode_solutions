// Last updated: 6/2/2025, 6:34:49 PM
class Solution {
 public:
  char findKthBit(int n, int k) {
    if (n == 1)
      return '0';
    const int midIndex = pow(2, n - 1);  // 1-indexed
    if (k == midIndex)
      return '1';
    if (k < midIndex)
      return findKthBit(n - 1, k);
    return findKthBit(n - 1, midIndex * 2 - k) == '0' ? '1' : '0';
  }
};