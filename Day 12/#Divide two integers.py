class Solution(object):
    def divide(self, dividend, divisor):
        
        if dividend == -2147483648 and divisor == -1: return 2147483647
        
        if dividend == 2147483647 and divisor == 1 : return 2147483647
        
        sign = (-1 if((dividend < 0) ^
                      (divisor < 0)) else 1);

        # remove sign of operands
        dividend = abs(dividend);
        divisor = abs(divisor);

        # Initialize
        # the quotient
        quotient = 0;
        temp = 0;

        # test down from the highest
        # bit and accumulate the
        # tentative value for valid bit
        for i in range(31, -1, -1):
            if (temp + (divisor << i) <= dividend):
                temp += divisor << i;
                quotient |= 1 << i;

        return sign * quotient;

