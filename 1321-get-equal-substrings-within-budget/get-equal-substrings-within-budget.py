class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        st = 0
        m = 0
        c = 0
        for i in range(len(s)):
            c += abs(ord(s[i]) - ord(t[i]))
            while c > maxCost:
                c -= abs(ord(s[st]) - ord(t[st]))
                st += 1
            m = max(m, i-st+1)
        return m
