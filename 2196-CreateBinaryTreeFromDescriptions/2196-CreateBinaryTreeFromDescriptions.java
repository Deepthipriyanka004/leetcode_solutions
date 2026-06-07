// Last updated: 6/7/2026, 11:12:31 AM
1class Solution {
2  public TreeNode createBinaryTree(int[][] descriptions) {
3    Map<TreeNode, TreeNode> childToParent = new HashMap<>();
4    Map<Integer, TreeNode> valToNode = new HashMap<>();
5
6    for (int[] d : descriptions) {
7      final int p = d[0];
8      final int c = d[1];
9      final int isLeft = d[2];
10      TreeNode parent = valToNode.getOrDefault(p, new TreeNode(p));
11      TreeNode child = valToNode.getOrDefault(c, new TreeNode(c));
12      valToNode.put(p, parent);
13      valToNode.put(c, child);
14      childToParent.put(child, parent);
15      if (isLeft == 1)
16        parent.left = child;
17      else
18        parent.right = child;
19    }
20
21    // Pick a random node and traverse upwardly.
22    TreeNode root = childToParent.keySet().iterator().next();
23    while (childToParent.containsKey(root))
24      root = childToParent.get(root);
25    return root;
26  }
27}