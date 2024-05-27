class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while i < len(word):
            c = word[i]
            co = 0
            while i + co < len(word) and word[i + co] == c and co < 9:
                co += 1
            comp += str(co) + c
            i += co
        return comp

