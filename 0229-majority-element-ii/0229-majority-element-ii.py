class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        counts = {}
        threshold = len(nums) // 3
        result = []
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        for num, freq in counts.items():
            if freq > threshold:
                result.append(num)
                
        return result
        