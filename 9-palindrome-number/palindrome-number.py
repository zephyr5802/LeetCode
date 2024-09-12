class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original_x = x
        reversed_int = 0
        
        while x != 0:
            digit = x % 10
            reversed_int = reversed_int * 10 + digit
            x //= 10
        
        return reversed_int == original_x

