# Last updated: 6/2/2025, 6:29:29 PM
class Solution:
    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def sumOfLargestPrimes(self, s: str) -> int:
        n = len(s)
        prime_set = set()

        for i in range(n):
            for j in range(i + 1, n + 1):
                num = int(s[i:j])  # leading zeros automatically handled
                if self.is_prime(num):
                    prime_set.add(num)

        top_primes = sorted(prime_set, reverse=True)
        return sum(top_primes[:3])
