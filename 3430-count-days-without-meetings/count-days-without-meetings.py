class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        def merge(intervals):
            if not intervals:
                return []
            intervals.sort(key=lambda x: x[0])
            m = [intervals[0]]
            for i in intervals[1:]:
                if i[0] <= m[-1][1]:
                    m[-1][1] = max(m[-1][1], i[1])
                else:
                    m.append(i)
            return m
        me = merge(meetings)
        to = 0
        for i, j in me:
            to += j - i +1
        a = days - to
        return a