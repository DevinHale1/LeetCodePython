class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = 121
        x = str(x)
        y = x[::-1]
        
        if x == y:
            return True
        else:
            return False
