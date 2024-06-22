class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        cu = sum(arr[:k])
        if cu / k >= float(threshold):
            c += 1
        for i in range(len(arr) - k):
            cu += (-1) * arr[i] + arr[i+k]
            if cu / k >= float(threshold):
                c += 1
        return c