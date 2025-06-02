# Last updated: 6/2/2025, 6:29:35 PM
MOD = 10**9 + 7

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        # Helper function to convert number x to base b
        def toBaseB(x, b):
            digits = []
            while x > 0:
                digits.append(x % b)
                x //= b
            return digits[::-1]
        
        # Helper function to count valid numbers with non-decreasing digits
        def count_up_to(digits, pos, last_digit, is_tight, memo):
            if pos == len(digits):  # Reached end of digits, this is a valid number
                return 1
            if (pos, last_digit, is_tight) in memo:
                return memo[(pos, last_digit, is_tight)]
            
            limit = digits[pos] if is_tight else b - 1
            result = 0
            for digit in range(last_digit, limit + 1):
                result += count_up_to(digits, pos + 1, digit, is_tight and (digit == limit), memo)
                result %= MOD
            
            memo[(pos, last_digit, is_tight)] = result
            return result
        
        # Function to count valid numbers from 0 to x
        def count_valid(x):
            if x < 0:
                return 0
            digits = toBaseB(x, b)
            memo = {}
            return count_up_to(digits, 0, 0, True, memo)
        
        # Convert l and r to integers
        l_int = int(l)
        r_int = int(r)
        
        # Final result is count_valid(r) - count_valid(l-1)
        return (count_valid(r_int) - count_valid(l_int - 1)) % MOD
