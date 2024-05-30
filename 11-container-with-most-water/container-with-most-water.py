class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r =  0,  n-1
        m = 0
        while  (l < r):
            w = min(height[l], height[r]) *(r-l)
            m = max(m, w)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m 