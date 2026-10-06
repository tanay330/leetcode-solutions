class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        tracker=0
        max_occurance=0
        for i in range(len(nums)):
            if nums[i]!=1:
                tracker=0
            else:    
                tracker+=1
                max_occurance=max(max_occurance,tracker)
        return max_occurance        
        