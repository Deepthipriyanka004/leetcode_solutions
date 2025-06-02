// Last updated: 6/2/2025, 6:32:11 PM
class Solution {
 public:
  int maximumCount(vector<int>& nums) {
    return max(ranges::count_if(nums, [](int num) { return num > 0; }),
               ranges::count_if(nums, [](int num) { return num < 0; }));
  }
};