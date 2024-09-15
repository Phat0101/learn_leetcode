class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while j < n:
            while nums2[j] > nums1[i] and i < m+j:
                i+=1
            nums1[i+1:m+j+1] = nums1[i:m+j]
            nums1[i] = nums2[j]
            j+=1