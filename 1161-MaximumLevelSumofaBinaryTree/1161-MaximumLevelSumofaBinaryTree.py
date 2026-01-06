# Last updated: 1/6/2026, 1:57:18 PM
1class Solution:
2  def maxLevelSum(self, root: TreeNode | None) -> int:
3    ans = 0
4    maxLevelSum = -math.inf
5    q = collections.deque([root])
6
7    level = 1
8    while q:
9      levelSum = 0
10      for _ in range(len(q)):
11        node = q.popleft()
12        levelSum += node.val
13        if node.left:
14          q.append(node.left)
15        if node.right:
16          q.append(node.right)
17      if levelSum > maxLevelSum:
18        maxLevelSum = levelSum
19        ans = level
20      level += 1
21
22    return ans