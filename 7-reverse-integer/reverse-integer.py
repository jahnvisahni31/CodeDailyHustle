class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            rev = int(str(x)[::-1])
        else:
            rev = -1 * int(str(x)[:0:-1])
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        else:
            return rev