# Last updated: 2/8/2026, 12:13:37 PM
1class Solution:
2  def isBalanced(self, root: TreeNode | None) -> bool:
3    if not root:
4      return True
5
6    def maxDepth(root: TreeNode | None) -> int:
7      if not root:
8        return 0
9      return 1 + max(maxDepth(root.left), maxDepth(root.right))
10
11    return (abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and
12            self.isBalanced(root.left) and
13            self.isBalanced(root.right))