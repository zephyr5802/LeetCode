class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Determine the sign of x
        sign = -1 if x < 0 else 1
        
        # Reverse the digits of the absolute value of x
        x = abs(x)
        reversed_x = 0
        
        # Reverse process
        while x != 0:
            # Get the last digit
            digit = x % 10
            # Update reversed_x by shifting the current digits and adding the last digit
            reversed_x = reversed_x * 10 + digit
            # Remove the last digit from x
            x //= 10
        
        # Apply the sign back to the reversed number
        reversed_x *= sign
        
        # Check for overflow or underflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
