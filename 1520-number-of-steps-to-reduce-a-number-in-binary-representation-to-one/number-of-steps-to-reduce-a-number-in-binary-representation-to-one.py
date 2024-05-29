class Solution:
    def numSteps(self, s: str) -> int:
        st = 0
        nu = int(s, 2)
        while nu != 1:
            if nu % 2 == 0:
                nu //= 2
            else:
                nu += 1
            st += 1
        return st