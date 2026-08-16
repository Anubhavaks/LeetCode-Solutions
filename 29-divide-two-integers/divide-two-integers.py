class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Edge case: Overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        dvd = abs(dividend)
        dvs = abs(divisor)
        quotient = 0

        # Bit shift approach
        while dvd >= dvs:
            temp_dvs = dvs
            multiple = 1
            
            # Double temp_dvs while it still fits into dvd
            while dvd >= (temp_dvs << 1):
                temp_dvs <<= 1
                multiple <<= 1

            dvd -= temp_dvs
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp result within 32-bit bounds
        return min(max(quotient, MIN_INT), MAX_INT)

        