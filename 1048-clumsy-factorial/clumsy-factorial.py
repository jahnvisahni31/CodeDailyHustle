class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n -= 1
        operations = ['*', '/', '+', '-']
        op_index = 0

        while n > 0:
            if operations[op_index] == '*':
                stack[-1] *= n
            elif operations[op_index] == '/':
                stack[-1] = int(stack[-1] / n)
            elif operations[op_index] == '+':
                stack.append(n)
            elif operations[op_index] == '-':
                stack.append(-n)

            n -= 1
            op_index = (op_index + 1) % 4

        return sum(stack)