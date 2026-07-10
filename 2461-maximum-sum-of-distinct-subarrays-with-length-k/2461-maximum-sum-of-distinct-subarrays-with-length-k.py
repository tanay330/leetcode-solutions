class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        res=0
        sum=0
        countDict=defaultdict(int)
        l=0
        for r in range(len(nums)):
            sum+=nums[r]
            countDict[nums[r]]+=1
            if r-l+1>k:
                countDict[nums[l]]-=1
                if countDict[nums[l]]==0:
                    countDict.pop(nums[l])
                sum-=nums[l]
                l+=1
            if len(countDict)==r-l+1==k:
                res=max(res,sum)
        return res                
                
          