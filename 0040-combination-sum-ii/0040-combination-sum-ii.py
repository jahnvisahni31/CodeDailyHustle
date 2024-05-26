class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        re = []
        candidates.sort()
        def ba(st, com, rem):
            if rem == 0:
                re.append(com[:])
                return
            if rem < 0:
                return
            for i in range(st, len(candidates)):
                if i > st and candidates[i] == candidates[i-1]:
                    continue
                com.append(candidates[i])
                ba(i+1,com, rem-candidates[i])
                com.pop()
        ba(0, [], target)
        return re