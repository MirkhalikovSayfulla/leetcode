class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            if num + current_sum > num:
                current_sum = num + current_sum
            else:
                current_sum = num
            
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum