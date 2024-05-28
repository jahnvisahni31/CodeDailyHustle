class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c_c = r_c = o_c = a_c = k_c = 0
        m = 0
        for c in croakOfFrogs:
            if c == "c":
                c_c += 1
            elif c == "r":
                r_c += 1
                if r_c > c_c:
                    return -1
            elif c == "o":
                o_c += 1
                if o_c > r_c:
                    return -1
            elif c == "a":
                a_c += 1
                if a_c > o_c:
                    return -1
            elif c == "k":
                k_c += 1
                if k_c > o_c:
                    return -1
            m = max(m, c_c - k_c)
        if c_c == r_c == o_c == a_c == k_c:
            return m
        else:
            return -1
