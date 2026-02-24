# Last updated: 2/24/2026, 7:04:47 PM
1class Solution:
2  def sumRootToLeaf(self, root: TreeNode | None) -> int:
3    ans = 0
4
5    def dfs(root: TreeNode | None, val: int) -> None:
6      nonlocal ans
7      if not root:
8        return
9      val = val * 2 + root.val
10      if not root.left and not root.right:
11        ans += val
12      dfs(root.left, val)
13      dfs(root.right, val)
14
15    dfs(root, 0)
16    return ans