class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        m = [[0 for _ in range(n)] for _ in range(n)]
        l, r,t ,b,nu = 0, n-1, 0, n-1,1
        while l <= r and t <= b:
            for i in range(l, r+1):
                m[t][i] = nu
                nu += 1
            t += 1
            for i in range(t, b+1):
                m[i][r] = nu
                nu += 1
            r -= 1
            if t <= b:
                for i in range(r , l-1, -1):
                    m[b][i] = nu
                    nu += 1
                b -= 1
            if l <= r:
                for i in range(b,t-1,-1):
                    m[i][l] = nu
                    nu += 1
                l += 1
        return m