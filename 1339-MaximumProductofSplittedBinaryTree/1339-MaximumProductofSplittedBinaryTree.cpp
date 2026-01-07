// Last updated: 1/7/2026, 9:44:38 PM
1class Solution {
2 public:
3  int maxProduct(TreeNode* root) {
4    constexpr int kMod = 1'000'000'007;
5    long ans = 0;
6    vector<int> allSums;
7    const long totalSum = treeSum(root, allSums);
8
9    for (const long sum : allSums)
10      ans = max(ans, sum * (totalSum - sum));
11
12    return ans % kMod;
13  }
14
15 private:
16  int treeSum(TreeNode* root, vector<int>& allSums) {
17    if (root == nullptr)
18      return 0;
19
20    const int leftSum = treeSum(root->left, allSums);
21    const int rightSum = treeSum(root->right, allSums);
22    const int sum = root->val + leftSum + rightSum;
23    allSums.push_back(sum);
24    return sum;
25  }
26};
27
28
29