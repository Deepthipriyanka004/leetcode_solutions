# Last updated: 3/15/2026, 9:36:26 AM
1class Fancy:
2  def __init__(self):
3    self.MOD = 1_000_000_007
4    # For each `val` in `vals`, it actually represents a * val + b.
5    self.vals = []
6    self.a = 1
7    self.b = 0
8
9  # To undo a * val + b and get the original value, we append (val - b) // a.
10  # By Fermat's little theorem:
11  #   a^(p - 1) ≡ 1 (mod p)
12  #   a^(p - 2) ≡ a^(-1) (mod p)
13  # So, (val - b) / a ≡ (val - b) * a^(p - 2) (mod p)
14  def append(self, val: int) -> None:
15    x = (val - self.b + self.MOD) % self.MOD
16    self.vals.append(x * pow(self.a, self.MOD - 2, self.MOD))
17
18  # If the value is a * val + b, then the value after adding by `inc` will be
19  # a * val + b + inc. So, we adjust b to b + inc.
20  def addAll(self, inc: int) -> None:
21    self.b = (self.b + inc) % self.MOD
22
23  # If the value is a * val + b, then the value after multiplying by `m` will
24  # be a * m * val + b * m. So, we adjust a to a * m and b to b * m.
25  def multAll(self, m: int) -> None:
26    self.a = (self.a * m) % self.MOD
27    self.b = (self.b * m) % self.MOD
28
29  def getIndex(self, idx: int) -> int:
30    return (-1 if idx >= len(self.vals)
31            else (self.a * self.vals[idx] + self.b) % self.MOD)