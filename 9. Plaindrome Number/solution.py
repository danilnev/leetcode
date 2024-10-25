class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not isinstance(x, int) or isinstance(x, bool):
            raise TypeError
        
        return str(x) == str(x)[::-1]

