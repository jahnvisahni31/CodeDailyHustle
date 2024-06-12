class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        c_s = [0]*256
        c_t = [0] * 256
        for i in range(len(s)):
            c_s[ord(s[i])] += i
            c_t[ord(t[i])] += i
        if c_s == c_t:
            return 0
        else:
            di = sum(abs(c_s[i]- c_t[i]) for i in range(256))
            return di