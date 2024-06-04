class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = set()
        r = 0
        for cj in s:
            if cj in c:
                r += 2
                c.remove(cj)
            else:
                c.add(cj)
        if len(c) > 0:
            r += 1
        return r