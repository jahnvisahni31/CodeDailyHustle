class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        p = 0
        t = len(profits)
        p1 = list(zip(capital, profits))
        p1.sort()
        m = []
        for c in range(k):
            while p < t and p1[p][0] <= w:
                heapq.heappush(m, -p1[p][1])
                p += 1
            if not m:
                return w
            w -= heapq.heappop(m)
        return w