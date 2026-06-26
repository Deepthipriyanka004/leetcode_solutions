# Last updated: 6/26/2026, 9:00:39 PM
1class BinaryIndexedTree:
2    __slots__ = "n", "c"
3
4    def __init__(self, n: int):
5        self.n = n
6        self.c = [0] * (n + 1)
7
8    def update(self, x: int, delta: int) -> None:
9        while x <= self.n:
10            self.c[x] += delta
11            x += x & -x
12
13    def query(self, x: int) -> int:
14        s = 0
15        while x:
16            s += self.c[x]
17            x -= x & -x
18        return s
19
20
21class Solution:
22    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
23        n = len(nums)
24        tree = BinaryIndexedTree(n * 2 + 1)
25        s = n + 1
26        tree.update(s, 1)
27        ans = 0
28        for x in nums:
29            s += 1 if x == target else -1
30            ans += tree.query(s - 1)
31            tree.update(s, 1)
32        return ans