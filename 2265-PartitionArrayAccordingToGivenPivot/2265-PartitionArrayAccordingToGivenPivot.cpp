// Last updated: 6/2/2025, 6:33:13 PM
class Solution {
 public:
  vector<int> pivotArray(vector<int>& nums, int pivot) {
    vector<int> ans;

    for (const int num : nums)
      if (num < pivot)
        ans.push_back(num);

    for (const int num : nums)
      if (num == pivot)
        ans.push_back(num);

    for (const int num : nums)
      if (num > pivot)
        ans.push_back(num);

    return ans;
  }
};