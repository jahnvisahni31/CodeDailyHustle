class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = 0
        re = 0
        isf = [0] * n
        for i in range(n):
            if i >= k:
                f ^= isf[i-k]
            if f == nums[i]:
                if i+k > n:
                    return -1
                isf[i] = 1
                f ^= 1
                re += 1
        return re