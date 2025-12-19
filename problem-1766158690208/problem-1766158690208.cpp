// Last updated: 12/19/2025, 9:08:10 PM
1class UnionFind {
2 public:
3  UnionFind(int n) : id(n), rank(n) {
4    iota(id.begin(), id.end(), 0);
5  }
6
7  void unionByRank(int u, int v) {
8    const int i = find(u);
9    const int j = find(v);
10    if (i == j)
11      return;
12    if (rank[i] < rank[j]) {
13      id[i] = j;
14    } else if (rank[i] > rank[j]) {
15      id[j] = i;
16    } else {
17      id[i] = j;
18      ++rank[j];
19    }
20  }
21
22  bool connected(int u, int v) {
23    return find(u) == find(v);
24  }
25
26  void reset(int u) {
27    id[u] = u;
28  }
29
30 private:
31  vector<int> id;
32  vector<int> rank;
33
34  int find(int u) {
35    return id[u] == u ? u : id[u] = find(id[u]);
36  }
37};
38
39class Solution {
40 public:
41  vector<int> findAllPeople(int n, vector<vector<int>>& meetings,
42                            int firstPerson) {
43    vector<int> ans;
44    UnionFind uf(n);
45    map<int, vector<pair<int, int>>> timeToPairs;
46
47    uf.unionByRank(0, firstPerson);
48
49    for (const vector<int>& meeting : meetings) {
50      const int x = meeting[0];
51      const int y = meeting[1];
52      const int time = meeting[2];
53      timeToPairs[time].push_back({x, y});
54    }
55
56    for (const auto& [_, pairs] : timeToPairs) {
57      unordered_set<int> peopleUnioned;
58      for (const auto& [x, y] : pairs) {
59        uf.unionByRank(x, y);
60        peopleUnioned.insert(x);
61        peopleUnioned.insert(y);
62      }
63      for (const int person : peopleUnioned)
64        if (!uf.connected(person, 0))
65          uf.reset(person);
66    }
67
68    for (int i = 0; i < n; ++i)
69      if (uf.connected(i, 0))
70        ans.push_back(i);
71
72    return ans;
73  }
74};
75