class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()
        i = 0
        for n in nums:
            if n in pair:
                return [pair[n], i]
            else:
                pair[target-n] = i
                i += 1