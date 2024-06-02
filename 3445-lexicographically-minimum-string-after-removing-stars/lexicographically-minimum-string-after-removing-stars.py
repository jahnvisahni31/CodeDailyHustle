class Solution:
    def clearStars(self, s: str) -> str:
        h, d = [], set()
        for i , j in enumerate(s):
            if j != "*":
                heappush(h, (ord(j), -i))
            else:
                v = heappop(h)[1]
                d.add(-v)
        an = ''
        for i , j in enumerate(s):
            if i not in d and j != "*":
                an += j
        return an