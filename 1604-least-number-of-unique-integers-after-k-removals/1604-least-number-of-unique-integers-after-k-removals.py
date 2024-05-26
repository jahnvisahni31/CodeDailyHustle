class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        while count and count[-1][1] <= k:
            k -= count.pop()[1]
        return len(count)
        