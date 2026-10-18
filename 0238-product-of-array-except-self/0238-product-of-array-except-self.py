class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n=len(nums)
        l1=[1]*n
        left_prod=1
        for i in range(n):
            l1[i]=left_prod
            left_prod*=nums[i]
        right_prod=1
        for i in range(n-1,-1,-1):
            l1[i]*=right_prod    
            right_prod*=nums[i]
                
        return l1            

        