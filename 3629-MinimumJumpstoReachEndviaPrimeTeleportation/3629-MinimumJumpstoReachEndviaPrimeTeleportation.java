// Last updated: 5/8/2026, 9:39:59 PM
1class Solution {
2    private static final int mx = 1000001;
3    private static final List<Integer>[] factors = new List[mx];
4
5    static {
6        for (int i = 0; i < mx; i++) {
7            factors[i] = new ArrayList<>();
8        }
9        for (int i = 2; i < mx; i++) {
10            if (factors[i].isEmpty()) {
11                for (int j = i; j < mx; j += i) {
12                    factors[j].add(i);
13                }
14            }
15        }
16    }
17
18    public int minJumps(int[] nums) {
19        int n = nums.length;
20        Map<Integer, List<Integer>> g = new HashMap<>();
21        for (int i = 0; i < n; i++) {
22            int x = nums[i];
23            for (int p : factors[x]) {
24                g.computeIfAbsent(p, k -> new ArrayList<>()).add(i);
25            }
26        }
27        int ans = 0;
28        boolean[] vis = new boolean[n];
29        vis[0] = true;
30        Deque<Integer> q = new ArrayDeque<>();
31        q.offer(0);
32        while (true) {
33            Deque<Integer> nq = new ArrayDeque<>();
34            for (int i : q) {
35                if (i == n - 1) {
36                    return ans;
37                }
38                List<Integer> idx = g.getOrDefault(nums[i], new ArrayList<>());
39                idx.add(i + 1);
40                if (i > 0) {
41                    idx.add(i - 1);
42                }
43                for (int j : idx) {
44                    if (!vis[j]) {
45                        vis[j] = true;
46                        nq.offer(j);
47                    }
48                }
49                idx.clear();
50            }
51            q = nq;
52            ans++;
53        }
54    }
55}