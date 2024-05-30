class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
    
    # Calculate the left products and store them in answer
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
    
    # Calculate the right products and update answer
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
    
        return answer
