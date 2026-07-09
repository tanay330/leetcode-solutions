class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        sum=0
        r=0
        for num in nums:
            sum+=num
        for i in range(len(nums)):
            r=sum-nums[i]-l
           
            if l==r:
                return i
            l+=nums[i]    
        return -1    


        