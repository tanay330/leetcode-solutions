class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        actual_sum=n*(n+1)//2
        arr_sum=0
        for i in range(n):
            arr_sum+=nums[i]
        missingNumber=actual_sum-arr_sum
        return missingNumber    
        