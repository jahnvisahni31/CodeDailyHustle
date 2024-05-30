class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        r = [False] * n
        m = max(candies)
        for i in range(n):
            t = candies[i] + extraCandies
            r[i] = (t >= m)
        return r