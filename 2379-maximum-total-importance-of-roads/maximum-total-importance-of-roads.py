class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        re = 0
        co = 1
        con = [0]*n
        for r in roads:
            con[r[0]] += 1
            con[r[1]] += 1
        con.sort()
        for c in con:
            re += c * co
            co += 1
        return re