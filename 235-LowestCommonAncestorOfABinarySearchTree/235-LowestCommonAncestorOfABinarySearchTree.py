# Last updated: 6/2/2025, 6:38:19 PM
class Solution:
  def lowestCommonAncestor(
      self,
      root: 'TreeNode',
      p: 'TreeNode',
      q: 'TreeNode',
  ) -> 'TreeNode':
    if root.val > max(p.val, q.val):
      return self.lowestCommonAncestor(root.left, p, q)
    if root.val < min(p.val, q.val):
      return self.lowestCommonAncestor(root.right, p, q)
    return root