class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a = []
        p = []
        v = [False] * len(nums)
        def ba():
            if len(p) == len(nums):
                a.append(p[:])
                return
            u = set()
            for i in range(len(nums)):
                if not v[i] and nums[i] not in u:
                    v[i] = True
                    p.append(nums[i])
                    u.add(nums[i])
                    ba()
                    v[i] = False
                    p.pop()
        ba()
        return a