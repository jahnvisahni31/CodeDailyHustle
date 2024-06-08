class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        su = {0: -1}
        r = 0
        for i , nu in enumerate(nums):
            r += nu
            if k != 0:
                r %= k
            if r in su:
                if i-su[r] > 1:
                    return True
            else:
                su[r] = i
        return False