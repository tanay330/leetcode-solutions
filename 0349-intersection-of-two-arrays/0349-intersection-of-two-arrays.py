class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l1=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums2[j] not in l1:
                        l1.append(nums2[j])
        return l1            
        