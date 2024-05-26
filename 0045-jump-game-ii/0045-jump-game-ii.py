class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        j = 0
        c = 0
        cu = 0
        for i in range(n-1):
            cu = max(cu, i+nums[i])
            if i == c:
                j += 1
                c = cu
        return j