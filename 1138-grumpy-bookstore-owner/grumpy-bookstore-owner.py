class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        a = 0
        t = sum((1-grumpy[i]) * customers[i] for i in range(len(customers)))
        w_a = 0
        w_p = 0
        for i in range(len(customers)):
            w_a += customers[i]
            w_p += (1- grumpy[i]) * customers[i]
            if i + 1 >= minutes:
                a = max(a, t- w_p + w_a)
                l = i - minutes + 1
                w_a -= customers[l]
                w_p -= (1-grumpy[l]) * customers[l]
        return a