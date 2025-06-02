// Last updated: 6/2/2025, 6:30:32 PM
class Solution {
 public:
  bool isArraySpecial(vector<int>& nums) {
    for (int i = 1; i < nums.size(); ++i)
      if (nums[i] % 2 == nums[i - 1] % 2)
        return false;
    return true;
  }
};