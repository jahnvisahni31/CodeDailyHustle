class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        re = []
        c = intervals[0]
        for i in intervals[1:]:
            if i[0] <= c[1]:
                c[1] = max(c[1], i[1])
            else:
                re.append(c)
                c = i
        re.append(c)
        return re