// Last updated: 6/2/2025, 6:33:04 PM
class Solution {
 public:
  int minBitFlips(unsigned start, unsigned goal) {
    return popcount(start ^ goal);
  }
};