# Last updated: 4/22/2026, 5:30:56 PM
1class Solution:
2    def twoEditWords(self, queries, dictionary):
3        def get_diff(q, w):
4            diff = 0
5            for i in range(len(q)):
6                if q[i] != w[i]:
7                    diff += 1
8                    if diff > 2:  # early stop
9                        return diff
10            return diff
11
12        ans = []
13
14        for query in queries:
15            for word in dictionary:
16                if len(query) != len(word):
17                    continue
18                
19                if get_diff(query, word) < 3:
20                    ans.append(query)
21                    break
22
23        return ans