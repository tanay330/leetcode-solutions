class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
          
        count=0
        map={0:1}
        prefix_sum=0

        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in map:
                count+=map[prefix_sum-k]
            map[prefix_sum]=map.get(prefix_sum,0)+1

      
      
      
      
        return count           