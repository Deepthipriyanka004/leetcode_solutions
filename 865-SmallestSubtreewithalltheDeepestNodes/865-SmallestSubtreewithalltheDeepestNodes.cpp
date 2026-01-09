// Last updated: 1/9/2026, 5:12:32 PM
1struct T {
2  TreeNode* lca;
3  int depth;
4};
5
6class Solution {
7 public:
8  TreeNode* subtreeWithAllDeepest(TreeNode* root) {
9    return dfs(root).lca;
10  }
11
12 private:
13  T dfs(TreeNode* root) {
14    if (root == nullptr)
15      return {nullptr, 0};
16
17    const T left = dfs(root->left);
18    const T right = dfs(root->right);
19    if (left.depth > right.depth)
20      return {left.lca, left.depth + 1};
21    if (left.depth < right.depth)
22      return {right.lca, right.depth + 1};
23    return {root, left.depth + 1};
24  }
25};