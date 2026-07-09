class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        prefix[0]=0
        suffix[len(nums)-1]=0
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j]=suffix[j+1]+nums[j+1]
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i

        return -1    


        