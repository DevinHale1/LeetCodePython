class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import sys
        y = ""
        x = str(x)
        
        if x[0] == "-":
            x = x[1:]
            y = x[::-1] 
            z = int(y)
            z = z * -1
            
            if z > 2**31 -1 or z < -2**31 :
                return 0
            else:
                return z
        else:
            y = x[::-1]
            z = int(y)
            if z > 2**31 -1 or z < -2**31 :
                return 0
            else:
                return z

        
