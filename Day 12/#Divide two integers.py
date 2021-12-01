
class Solution(object):
    def divide(self, dividend, divisor):
        
        if dividend == -2147483648 and divisor == -1: return 2147483647
        
        if dividend == 2147483647 and divisor == 1 : return 2147483647
        
        sign = (-1 if((dividend < 0) ^
                      (divisor < 0)) else 1);

        
        a = abs(dividend);
        b = abs(divisor);
        res = 0
        
        while(a-b>=0):
            x = 0 # 2^0 = 1
            
            while(a-(b<<1<<x) >= 0):
                x += 1
            
            res += 1<<x
            a -= b<<x
        return res*sign

