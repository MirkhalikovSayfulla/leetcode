class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[start]:
                if target >= nums[start] and target < nums[mid]: 
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1
                
        return False