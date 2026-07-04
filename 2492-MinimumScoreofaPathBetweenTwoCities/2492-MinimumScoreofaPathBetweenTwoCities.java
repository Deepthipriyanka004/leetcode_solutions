// Last updated: 7/4/2026, 9:09:45 AM
1class Solution {
2  public int minScore(int n, int[][] roads) {
3    int ans = Integer.MAX_VALUE;
4    List<Pair<Integer, Integer>>[] graph = new List[n]; // graph[u] := [(v, distance)]
5    Queue<Integer> q = new ArrayDeque<>(List.of(0));
6    boolean[] seen = new boolean[n];
7    seen[0] = true;
8    Arrays.setAll(graph, i -> new ArrayList<>());
9
10    for (final int[] r : roads) {
11      final int u = r[0] - 1;
12      final int v = r[1] - 1;
13      final int distance = r[2];
14      graph[u].add(new Pair<>(v, distance));
15      graph[v].add(new Pair<>(u, distance));
16    }
17
18    while (!q.isEmpty()) {
19      final int u = q.poll();
20      for (Pair<Integer, Integer> pair : graph[u]) {
21        final int v = pair.getKey();
22        final int d = pair.getValue();
23        ans = Math.min(ans, d);
24        if (seen[v])
25          continue;
26        q.offer(v);
27        seen[v] = true;
28      }
29    }
30
31    return ans;
32  }
33}