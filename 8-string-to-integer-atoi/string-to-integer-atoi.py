class Solution:
    def myAtoi(self, s: str) -> int:
        length, i, sign, res = len(s), 0, 1, 0

        # Skip leading whitespaces
        while i < length and s[i] == ' ':
            i += 1

        # Check for optional sign
        if i < length and s[i] in ('-', '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert digits to integer
        while i < length and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        # Apply sign and handle out of bounds
        res = sign * res
        return max(-2**31, min(res, 2**31 - 1))