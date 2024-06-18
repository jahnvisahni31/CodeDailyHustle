class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m = max(difficulty)
        m_u = [0] * (m + 1)
        for d, p in zip(difficulty, profit):
            m_u[d] = max(m_u[d], p)
        for i in range(1, m+1):
            m_u[i] = max(m_u[i], m_u[i-1])
        t = 0
        for ab in worker:
            if ab > m:
                t += m_u[m]
            else:
                t += m_u[ab]
        return t