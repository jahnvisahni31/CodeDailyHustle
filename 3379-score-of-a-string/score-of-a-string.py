class Solution:
    def scoreOfString(self, s: str) -> int:
        t = 0
        for i in range(1 , len(s)):
            sf = abs(ord(s[i]) - ord(s[i-1]))
            t += sf
        return t