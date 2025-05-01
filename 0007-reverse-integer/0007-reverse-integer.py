class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        
        if x < 0:
            x_str = x_str[1:] 
            x_str = '-' + x_str[::-1]  
        else:
            x_str = x_str[::-1]

        res = int(x_str)
        if ((res > (2**31 - 1)) or (res < -2**31)):
            return 0
        
        return res