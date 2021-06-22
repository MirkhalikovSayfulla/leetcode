class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = count1 = count2 = 0
        for  i  in range(len(nums)):
            if nums[i] == 0: 
                count0+=1
            if nums[i] == 1:
                count1+=1
            if nums[i] == 2:
                count2+=1
                
        for i in range(len(nums)):
            if i < count0:
                nums[i] = 0
            elif i < count0 + count1:
                nums[i] = 1
            else:
                nums[i] = 2
    

        