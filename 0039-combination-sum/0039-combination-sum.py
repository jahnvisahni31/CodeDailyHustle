class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        re = []
        def ba(st, com, rem):
            if rem == 0:
                re.append(com[:])
                return
            if rem < 0:
                return
            for i in range(st, len(candidates)):
                com.append(candidates[i])
                ba(i,com, rem-candidates[i])
                com.pop()
        ba(0, [], target)
        return re