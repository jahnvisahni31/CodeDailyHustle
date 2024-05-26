class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1,-1, -1):
            digits[i] += c
            if digits[i] < 10:
                c = 0
                break
            else:
                digits[i] = 0
        if c == 1:
            digits = [1] + digits
        return digits