class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = float('inf')
        i=0
        j=0
        total=0
        while j<len(nums):
            total+=nums[j]

            while total>=target:
                size=min(size,j-i+1)
                total-=nums[i]
                i+=1
           
                
            j+=1
        return 0 if size== float('inf') else size    

        