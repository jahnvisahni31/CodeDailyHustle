class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def back(index, path):
            if index == len(digits):
                re.append(''.join(path))
                return
            c = digits[index]
            for l in mapping[c]:
                path.append(l)
                back(index+1, path)
                path.pop()
        re = []
        back(0, [])
        return re