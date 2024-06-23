class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for i in words:
            l=len(i)
            if s[:l] == i:
                count=count+1
        return count