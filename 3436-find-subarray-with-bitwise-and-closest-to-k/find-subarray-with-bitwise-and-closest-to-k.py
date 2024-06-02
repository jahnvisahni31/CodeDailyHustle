class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        s = set([(1 << 40)-1])
        an = 1e9
        for x in nums:
            s = {y&x for y in s} | {(1<<40)-1}
            for n in s:
                an = min(an, abs(n-k))
        return an