class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        mid=0
        right=len(nums)-1
        while mid<=right:
            if nums[mid]==0:
                nums[start],nums[mid]=nums[mid],nums[start]
                start+=1
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
            else:
                mid+=1       
        