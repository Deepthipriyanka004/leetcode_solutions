# Last updated: 6/2/2025, 6:36:15 PM
class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    def mergeSort(A: List[int], l: int, r: int) -> None:
      if l >= r:
        return

      def merge(A: List[int], l: int, m: int, r: int) -> None:
        sorted = [0] * (r - l + 1)
        k = 0  
        i = l  
        j = m + 1  

        while i <= m and j <= r:
          if A[i] < A[j]:
            sorted[k] = A[i]
            k += 1
            i += 1
          else:
            sorted[k] = A[j]
            k += 1
            j += 1

        
        while i <= m:
          sorted[k] = A[i]
          k += 1
          i += 1

        
        while j <= r:
          sorted[k] = A[j]
          k += 1
          j += 1

        A[l:l + len(sorted)] = sorted

      m = (l + r) // 2
      mergeSort(A, l, m)
      mergeSort(A, m + 1, r)
      merge(A, l, m, r)

    mergeSort(nums, 0, len(nums) - 1)
    return nums