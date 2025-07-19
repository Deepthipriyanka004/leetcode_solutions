# Last updated: 7/19/2025, 9:45:29 AM
class Solution:
  def removeSubfolders(self, folder: list[str]) -> list[str]:
    ans = []
    prev = ""

    folder.sort()

    for f in folder:
      if len(prev) > 0 and f.startswith(prev) and f[len(prev)] == '/':
        continue
      ans.append(f)
      prev = f

    return ans