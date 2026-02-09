# Last updated: 2/9/2026, 10:36:54 AM
1class Solution:
2    def balanceBST(self, root):
3        nums = []
4        self.inorder(root, nums)
5        return self.build(nums, 0, len(nums) - 1)
6
7    def inorder(self, root, nums):
8        if not root:
9            return
10        self.inorder(root.left, nums)
11        nums.append(root.val)
12        self.inorder(root.right, nums)
13
14    def build(self, nums, l, r):
15        if l > r:
16            return None
17        m = (l + r) // 2
18        node = TreeNode(nums[m])
19        node.left = self.build(nums, l, m - 1)
20        node.right = self.build(nums, m + 1, r)
21        return node
22