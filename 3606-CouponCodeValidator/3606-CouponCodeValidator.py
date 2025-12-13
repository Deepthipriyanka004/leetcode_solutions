# Last updated: 12/13/2025, 9:45:01 AM
1class Solution:
2    def validateCoupons(
3        self, code: List[str], businessLine: List[str], isActive: List[bool]
4    ) -> List[str]:
5        """
6        Validates and returns sorted coupon codes based on specific criteria.
7      
8        Args:
9            code: List of coupon codes to validate
10            businessLine: List of business lines corresponding to each coupon
11            isActive: List of boolean flags indicating if each coupon is active
12          
13        Returns:
14            List of valid coupon codes sorted by business line and then by code
15        """
16      
17        def is_valid_code(coupon_code: str) -> bool:
18            """
19            Checks if a coupon code contains only alphanumeric characters and underscores.
20          
21            Args:
22                coupon_code: The coupon code string to validate
23              
24            Returns:
25                True if the code is valid, False otherwise
26            """
27            # Empty strings are invalid
28            if not coupon_code:
29                return False
30          
31            # Check each character is alphanumeric or underscore
32            for char in coupon_code:
33                if not (char.isalpha() or char.isdigit() or char == "_"):
34                    return False
35          
36            return True
37      
38        # Define valid business lines
39        valid_business_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
40      
41        # Collect indices of valid coupons
42        valid_indices = []
43      
44        # Iterate through all coupons with their index
45        for index, (coupon_code, business, is_active_flag) in enumerate(
46            zip(code, businessLine, isActive)
47        ):
48            # Check all validation criteria:
49            # 1. Coupon must be active
50            # 2. Business line must be in the valid set
51            # 3. Coupon code must pass character validation
52            if (is_active_flag and 
53                business in valid_business_lines and 
54                is_valid_code(coupon_code)):
55                valid_indices.append(index)
56      
57        # Sort indices by business line first, then by coupon code
58        valid_indices.sort(key=lambda i: (businessLine[i], code[i]))
59      
60        # Return the sorted list of valid coupon codes
61        return [code[i] for i in valid_indices]